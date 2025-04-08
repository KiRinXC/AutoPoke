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

# from Scripts.PokeM02 import PokeM02
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# Poke = PokeM02("喵喵刮鳞聚宝")
# Poke.run()

# from Scripts.PokeA01 import PokeA01
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# move_set = {'direction': ['a', 'd'], 'is_specified': False}
# turn_set = {'direction': ['w', 's'], 'is_specified': True}
# Poke = PokeA01("单遇刷闪",move_set,turn_set)
# Poke.run()


# from Scripts.PokeA02 import PokeA02
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# move_set = {'direction': ['w', 's'], 'is_specified': False}
# turn_set = {'direction': ['d', 'a'], 'is_specified': True}
# Poke = PokeA02("香水刷闪",move_set,turn_set)
# Poke.run()
#

# from Scripts.PokeA03 import PokeA03
# from AutoControl.Security.logging import setup_logging
# from AutoControl.Security.encoder import Encoder
# setup_logging()
# encoder = Encoder("Spray-Keys", "SA03")
# client_key, server_key, _ = encoder.run()
# move_set = {'direction': ['d', 'a'], 'is_specified': False}
# turn_set = {'direction': ['w', 's'], 'is_specified': True}
# Poke = PokeA03("喷雾刷闪",move_set,turn_set)
# Poke.threads.remove(Poke.turn)
# Poke.run()






# from Scripts.PokeC02 import PokeC02
# from AutoControl.Security.logging import setup_logging
#
# setup_logging()
# move_set = {'direction': ['s', 'w'], 'is_specified': True}
# turn_set = {'direction': ['d', 'a'], 'is_specified': True}
# Poke = PokeC02("抓公虫", move_set, turn_set)
# Poke.run()

# from Scripts.PokeC01 import PokeC01
# from AutoControl.Security.logging import setup_logging
# setup_logging()
# move_set = {'direction': ['w', 's'], 'is_specified': True}
# turn_set = {'direction': ['d', 'a'], 'is_specified':True}
# Poke = PokeC01("抓蘑菇",move_set,turn_set)
# Poke.run()

# from Scripts.PokeC03 import PokeC03
# from AutoControl.Security.logging import setup_logging
# from AutoControl.Security.encoder import Encoder
# setup_logging()
# encoder = Encoder("Ditto-Keys", "SC03")
# client_key, server_key, _ = encoder.run()
# move_set = {'direction': ['d', 'a'], 'is_specified': False}
# turn_set = {'direction': ['w', 's'], 'is_specified': False}
# Poke = PokeC03("抓百变",move_set,turn_set)
# Poke.threads.remove(Poke.turn)
# Poke.run()

# from Scripts.PokeA04 import PokeA04
# from AutoControl.Security.logging import setup_logging
# from AutoControl.Security.encoder import Encoder
# setup_logging()
# encoder = Encoder("Monsters-Keys", "SA04")
# client_key, server_key, _ = encoder.run()
# Poke = PokeA04("群怪刷闪")
# Poke.run()


from Scripts.PokeA06 import PokeA06
from AutoControl.Security.encoder import Encoder
from AutoControl.Security.logging import setup_logging
encoder = Encoder("Hatching-Eggs-Keys", "SA06")
client_key, server_key, _ = encoder.run()
setup_logging()
Poke = PokeA06("孵蛋")
Poke.run()
