from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QResource  # 导入 QResource

# 在 QApplication 之前先实例化
uiLoader = QUiLoader()

class Stats:

    def __init__(self):
        # 加载资源文件
        QResource.registerResource("./assets/UIcon.qrc")  # 假设资源文件名为 UI/UIcon.qrc
        # 再加载界面
        self.ui = uiLoader.load('UI/AutoPokeUI.ui')

        self.keys()

    def keys(self):
        self.ui.LaunchButtonA_1.clicked.connect(self.cc)

    def cc(self):
        print("hello")
    # 其它代码 ...

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec()