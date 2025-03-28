from AutoControl.Utili.web.sendRemind import send_remind
from AutoControl.Utili.control.screenShot import screen_shot
def remind_shiny():
    """
    出闪提醒
    """
    # 先发提醒
    send_remind()
    #再截图
    screen_shot()





