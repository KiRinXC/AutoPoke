# from PySide6.QtWidgets import QApplication, QMessageBox
# from PySide6.QtUiTools import QUiLoader
#
# # 在QApplication之前先实例化
# uiLoader = QUiLoader()
#
# class Stats:
#
#     def __init__(self):
#         # 再加载界面
#         self.ui = uiLoader.load('TestUI.ui')
#
#
# app = QApplication([])
# stats = Stats()
# stats.ui.show()
# app.exec() # PySide6 是 exec 而不是 exec_

# from Scripts.PokeM01 import PokeM01
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# Poke = PokeM01("彩幽刮鱼鳞")
# Poke.run()

# from Scripts.PokeA02 import PokeA02
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# move_set = {'direction': ['w', 's'], 'is_specified': False}
# turn_set = {'direction': ['d', 'a'], 'is_specified': True}
# Poke = PokeA02("香水刷闪",move_set,turn_set)
# Poke.run()

from Scripts.PokeC02 import PokeC02
from AutoControl.Security.logging import setup_logging
setup_logging()
move_set = {'direction': ['d', 'a'], 'is_specified': False}
turn_set = {'direction': ['w', 's'], 'is_specified': True}
Poke = PokeC02("抓公虫",move_set,turn_set)
Poke.run()

# from Scripts.PokeC03 import PokeC03
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# move_set = {'direction': ['d', 'a'], 'is_specified': False}
# turn_set = {'direction': ['w', 's'], 'is_specified': False}
# Poke = PokeC03("抓百变",move_set,turn_set)
# Poke.run()

#
# from Scripts.PokeA04 import PokeA04
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# Poke = PokeA04("群怪刷闪")
# Poke.run()