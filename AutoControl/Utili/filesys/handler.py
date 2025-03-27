import json
import os
from AutoControl.Utili.calculate.getRoot import get_root
import logging

class Handler(object):
    def __init__(self):
        # 获取项目的根目录
        root_dir = get_root()

        self.log= logging.getLogger(__name__)
        # 构建资源文件的绝对路径
        self.config_dir = os.path.join(root_dir, 'config')
        self.data_dir = os.path.join(root_dir, 'data')
        self.key_dir = os.path.join(root_dir, 'key')
        self.template_dir = os.path.join(root_dir, 'template')
        self.log_dir = os.path.join(root_dir, 'log')
        # 验证并创建所有目录
        self.create_directory(self.config_dir)
        self.create_directory(self.data_dir)
        self.create_directory(self.key_dir)
        self.create_directory(self.template_dir)
        self.create_directory(self.log_dir)

    # 定义一个函数来验证和创建目录
    def create_directory(self,dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # 加载JSON配置
    def download_json(self,file_name):
        config_path = os.path.join(self.config_dir, file_name+'.json')
        with open(config_path, 'r',encoding='utf-8') as config_file:
            return json.load(config_file)

    # 推送JSON配置
    def upload_json(self,file_name, data):
        config_path = os.path.join(self.config_dir,file_name+'.json')
        with open(config_path,'w',encoding='utf-8') as config_file:
            json.dump(data,config_file)


    # 加载刷闪数据
    def download_recode(self,file_name):
        record_path = os.path.join(self.data_dir, file_name + '.json')
        # 是否需要新建文件
        if not os.path.exists(record_path):
            # 新建文件
            data = {'poke_num': 0,'shiny_num': 0}
            with open(record_path, 'w', encoding='utf-8') as f:
                json.dump(data,f)
        # 然后再打开文件进行读取
        with open(record_path, 'r', encoding='utf-8') as f:
            poke_recode = json.load(f)
            poke_num = poke_recode["poke_num"]
            shiny_num = poke_recode["shiny_num"]
        return poke_num,shiny_num

    # 推送刷闪数据
    def upload_recode(self,file_name,poke_num,shiny_num):
        record_path = os.path.join(self.data_dir,file_name+'.json')
        data = {'poke_num': poke_num,'shiny_num': shiny_num}
        with open(record_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    # 构建模板图片的绝对路径
    def get_template_path(self,file_name):
        template_path = os.path.join(self.template_dir, f"{file_name}.png")
        if not os.path.exists(template_path):
            self.log.error("{}模板图片不存在")
            exit(1)
        return template_path


    def is_exist(self,file_name):
        """验证密钥文件是否存在"""
        path = os.path.join(self.key_dir, file_name + '.json')
        if not os.path.exists(path):
            return False
        else:
            return True

    # 下载密钥文件
    def download_key(self,file_name):
        key_path = os.path.join(self.key_dir, file_name+'.json')
        if not os.path.exists(key_path):
            data = {"client_key":"","server_key":"","derive_key":""}
            with open(key_path, 'w', encoding='utf-8') as f:
                json.dump(data,f)
        with open(key_path, 'r', encoding='utf-8') as f:
            keys = json.load(f)
        return keys

    # 推送密钥文件
    def upload_key(self,file_name,client_key,server_key,derive_key):
        key_path = os.path.join(self.key_dir,file_name+'.json')
        data = {"client_key":client_key,"server_key":server_key,"derive_key":derive_key}
        with open(key_path,'w',encoding='utf-8') as f:
            json.dump(data,f)





