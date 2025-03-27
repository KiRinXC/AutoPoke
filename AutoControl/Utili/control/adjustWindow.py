import pyautogui
import pygetwindow
from AutoControl.Utili.filesys.handler import Handler
def adjust_window():
    handler = Handler()
    '''
    调整窗口并激活
    '''
    Settings = handler.download_json('Settings')
    RegMouse = handler.download_json('RegMouse')
    RegDetect = handler.download_json('RegDetect')
    # 获取屏幕尺寸并添加至config中
    scr_x, scr_y = pyautogui.size()
    Settings["scr_size"] = [scr_x, scr_y]

    # 获取设定的缩放游戏窗口大小
    win_w, win_h = Settings["win_size"][0], Settings["win_size"][1]

    # 确定游戏界面的左上角起始坐标 并添加至config
    win_p_x, win_p_y = scr_x - win_w, 0
    RegMouse["reg_win"] = [win_p_x, win_p_y, win_w, win_h]
    RegDetect["reg_win"] = [win_p_x, win_p_y, win_w, win_h]

    # 更新config
    handler.upload_json("Settings", Settings)
    handler.upload_json("RegMouse", RegMouse)
    handler.upload_json("RegDetect", RegDetect)
    # 获取当前所有已开启的窗口
    windows = pygetwindow.getAllWindows()
    # PokeMMO窗口名称使用了部分西里尔字母进行编码，需要转换成拉丁字母
    trans_table = str.maketrans({
        'Р': 'P',
        'М': 'M',
        'е': 'e',
        'о': 'o'
    })
    for window in windows:
        # 将窗口的字符转换后在进行比较
        title_trans = window.title.translate(trans_table)
        if title_trans == "PokeMMO":
            # 激活窗口并调整大小和位置
            window.activate()
            window.resizeTo(win_w, win_h)
            window.moveTo(win_p_x, win_p_y)
            return window
    return False