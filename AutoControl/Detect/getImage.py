import mss
import numpy as np
from AutoControl.Utili.filesys.handler import Handler
handler = Handler()
reg_win= handler.download_json('RegDetect')["reg_win"]

def get_image(offset):
    """
    截取目标区域
    :param offset:
    :return: 数组表示的图像
    """
    left = reg_win[0] + offset[0]
    top = reg_win[1] + offset[1]
    width = offset[2]
    height = offset[3]
    # 使用 mss 截取屏幕区域
    with mss.mss() as sct:
        # mss截图出的图像格式为 BGR+Alpha
        image = sct.grab({"left": left, "top": top, "width": width, "height": height})
        # 只保留 BGR
        image_array = np.array(image)[:,:,:3]
    return image_array