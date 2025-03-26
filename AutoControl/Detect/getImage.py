import mss
import numpy as np

def get_image(base, offset):
    """
    截取目标区域
    :param base:
    :param offset:
    :return: 数组表示的图像
    """
    left = base[0] + offset[0]
    top = base[1] + offset[1]
    width = offset[2]
    height = offset[3]
    # 使用 mss 截取屏幕区域
    with mss.mss() as sct:
        # mss截图出的图像格式为 BGR+Alpha
        image = sct.grab({"left": left, "top": top, "width": width, "height": height})
        # 只保留 BGR
        image_array = np.array(image)[:,:,:3]
    return image_array