from datetime import datetime
import cv2

from AutoControl.Utili.filesys.handler import Handler
from AutoControl.Detect.getImage import get_image

def screen_shot():
    """
    截图
    """
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    time_now = f"{year}-{month}-{day}-{hour}-{minute}"
    handler = Handler()
    Settings = handler.download_json("Settings")
    win_size = Settings["win_size"]
    image_array = get_image([0,0,win_size[0],win_size[1]])
    # 使用 OpenCV 保存图像
    cv2.imwrite(f'{time_now}.png', image_array)



