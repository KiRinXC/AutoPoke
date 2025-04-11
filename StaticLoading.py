import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox

from AutoControl.Security.encoder import Encoder


from UI import Ui_Form  # 导入生成的 UI 类

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # 实例化生成的 UI 类
        self.ui.setupUi(self)  # 设置 UI
        self.password  = "SA01"
        self.encoder = Encoder("Keys",self.password)
        self.actionConnect()

    def actionConnect(self):
        self.ui.GetKeyButton.clicked.connect(self.getKey)
        self.ui.VerifyKeyButton.clicked.connect(self.verifyKey)

    def getKey(self):
        client_key=self.encoder.generate_client_key()
        self.ui.ClientKeylineEdit.setText(client_key)
        clipboard = QApplication.clipboard()  # 获取系统剪切板
        clipboard.setText(client_key)  # 将 client_key 复制到剪切板

    def verifyKey(self):
        client_key=self.ui.ClientKeylineEdit.text()
        server_key=self.ui.ServerKeylineEdit.text()
        result = self.encoder.init_keys(client_key, server_key)
        if result:
            # 弹窗显示激活信息
            start_date, duration, app_type = result
            QMessageBox.information(self, "激活成功", f"起始日期为 {start_date},激活天数{duration},脚本类型{app_type}")
        else:
            # 如果验证失败，弹窗提示错误信息
            QMessageBox.warning(self, "激活失败", "无法验证密钥，请检查输入是否正确！")




























if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())