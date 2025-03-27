import hashlib
import uuid
import os
import base64
from datetime import datetime
import logging

import wmi
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

from AutoControl.Utili.filesys.handler import Handler

class Encoder:
    def __init__(self,file_name,password):
        self.file_name = file_name
        self.password =password
        self.logger = logging.getLogger(__name__)

    def get_hardware_uuid(self):
        try:
            # 使用 WMI 获取主板 UUID
            c = wmi.WMI()
            for item in c.Win32_ComputerSystemProduct():
                return item.UUID
        except:
            self.logger.error(f"用户身份鉴别失败")
            exit(1)


    def get_machine_code(self):
        # 获取基于硬件地址的 UUID 并进行md5加密
        hardware_uuid = self.get_hardware_uuid()
        # 使用主板 UUID 生成稳定的 UUID
        return self.md5_encrypt(str(uuid.uuid5(uuid.NAMESPACE_DNS, hardware_uuid)))


    @staticmethod
    def generate_key(password: str, salt: bytes) -> bytes:
        """使用 PBKDF2 从密码和盐生成密钥"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,  # 生成 32 字节的密钥（AES-256）
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        return kdf.derive(password.encode())

    @staticmethod
    def get_current_date_in_format() -> str:
        """
        获取当前日期并格式化为 YYYYMMDD 的形式。
        """
        # 获取当前日期
        current_date = datetime.now()

        # 格式化为指定的字符串格式
        formatted_date = current_date.strftime("%Y%m%d")

        return formatted_date

    @staticmethod
    def md5_encrypt(input_string: str) -> str:
        """
        将输入字符串进行 MD5 加密，并返回 32 位的十六进制字符串。
        """
        # 创建一个 MD5 哈希对象
        md5_hash = hashlib.md5()

        # 更新哈希对象的内容（需要将字符串编码为字节）
        md5_hash.update(input_string.encode('utf-8'))

        # 获取哈希值的十六进制表示
        hex_digest = md5_hash.hexdigest()

        return str(hex_digest)


    def aes_encrypt(self, date: str, password: str) -> str:
        """加密日期并返回加密后的密码"""
        try:
            salt = os.urandom(16)  # 生成随机盐
            key = self.generate_key(password, salt)
            iv = os.urandom(16)  # 生成随机初始化向量

            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_date = encryptor.update(date.encode()) + encryptor.finalize()

            # 将加密结果、盐和初始化向量拼接后进行 Base64 编码
            encoded_result = base64.urlsafe_b64encode(salt + iv + encrypted_date).rstrip(b'=')
            return encoded_result.decode()
        except:
            self.logger.error(f"加密失败，密钥错误")
            exit(1)

    def aes_decrypt(self, encrypted_password: str, password: str) -> str:
        """解密加密后的密码并返回原始日期"""
        try:
            decoded_data = base64.urlsafe_b64decode(encrypted_password + '=' * (-len(encrypted_password) % 4))
            salt = decoded_data[:16]
            iv = decoded_data[16:32]
            encrypted_date = decoded_data[32:]

            key = self.generate_key(password, salt)
            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_date = decryptor.update(encrypted_date) + decryptor.finalize()
            return decrypted_date.decode()
        except:
            self.logger.error(f"解密失败，密钥错误")
            exit(1)

    def generate_client_key(self):
        """生成客户端密钥"""
        machine_code_encode = self.get_machine_code()
        return self.aes_encrypt(machine_code_encode,self.password)


    def verify_client_key(self,client_key):
        machine_code_encode = self.get_machine_code()
        current_key = self.aes_decrypt(client_key,self.password)
        if current_key == machine_code_encode:
            return current_key
        else:
            self.logger.error("客户端密钥验证失败")
            exit(1)


    def generate_server_key(self,client_key,password):
        """生成服务端密钥"""
        machine_code_encode = self.aes_decrypt(client_key,password)
        self.logger.info(f"machine_code_encode is {machine_code_encode}")
        date =self.get_current_date_in_format()
        password_encode = self.md5_encrypt(password+machine_code_encode)
        return self.aes_encrypt(date,password_encode)

    def verify_server_key(self,client_key,server_key):
        """从客户端密钥中得到起始日期"""
        machine_code_encode = self.verify_client_key(client_key)
        password_encode = self.md5_encrypt(self.password+machine_code_encode)
        start_date = self.aes_decrypt(server_key,password_encode)
        if start_date is not None:
            return start_date
        else:
            self.logger.error("服务端密钥验证失败")
            exit(1)

    def generate_derive_key(self,client_key,server_key):
        """生成派生密钥"""
        return self.aes_encrypt(client_key,server_key)

    def verify_derive_key(self,client_key,server_key,derive_key):
        current_client_key = self.aes_decrypt(derive_key,server_key)
        if current_client_key ==client_key:
            return True
        else:
            self.logger.error("派生密钥验证失败")
            exit(1)

    def verify_keys(self):
        """在UI中使用"""
        handler = Handler()
        if handler.is_exist(self.file_name):
            keys = handler.download_key(self.file_name)
            client_key = keys["client_key"]
            server_key = keys["server_key"]
            derive_key = keys["derive_key"]
            if self.verify_client_key(client_key) and self.verify_server_key(client_key,server_key) and self.verify_derive_key(client_key,server_key,derive_key):
                return client_key,server_key,derive_key

    def run(self):
        """新建或验证密钥文件"""
        handler = Handler()
        if handler.is_exist(self.file_name):
            keys = handler.download_key(self.file_name)
            client_key = keys["client_key"]
            server_key = keys["server_key"]
            derive_key = keys["derive_key"]
            if self.verify_client_key(client_key) and self.verify_server_key(client_key,server_key) and self.verify_derive_key(client_key,server_key,derive_key):
                return client_key,server_key,derive_key
        else:
            client_key = self.generate_client_key()
            print(client_key)
            server_key = input("请输入密钥：")
            if self.verify_server_key(client_key,server_key):
                derive_key = self.generate_derive_key(client_key,server_key)
                handler.upload_key(self.file_name,client_key,server_key,derive_key)
                return client_key,server_key,derive_key
            else:
                exit(1)

