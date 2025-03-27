import numpy as np
from AutoControl.Detect.getImage import get_image

"""
检测区域颜色时，都采用原图检测
"""
def is_all_black(offset):
    """
    检测全部偏移区域是否全黑，偏移区域可能不为1
    :param offset: 偏移
    :return:
    """
    for i in range(len(offset)):
        image_array = get_image(offset[i])
        # 检查是否全黑
        if not np.all(image_array <= 50):
            # 不是全黑则直接返回False
            return False
    return True


def is_any_black(offset):
    """
    检测偏移区域是否包含黑色
    :param offset: 偏移
    :return:
    """
    image_array = get_image(offset)
    # 检查是否有黑色
    return np.any(image_array <= 50)


def is_all_white(offset):
    """
    检测全部偏移区域是否全白，偏移区域可能不为1
    :param offset: 偏移
    :return:
    """
    for i in range(len(offset)):
        image_array = get_image(offset[i])
        # 检查是否全白
        if not np.all(image_array >= 245):
            # 不是全白则直接返回False
            return False
    return True


def is_any_white(offset):
    """
    检测偏移区域是否包含白色
    :param offset: 偏移
    :return:
    """
    image_array = get_image(offset)
    # 检查是否包含白色
    return np.any(image_array >= 245)




