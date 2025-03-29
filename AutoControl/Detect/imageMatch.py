import cv2
from AutoControl.Detect.getImage import get_image


def image_match(templates, offset, is_ocr):
    """
    判断图像中是否存在模板图片
    :param templates: 模板的多个绝对路径
    :param offset:偏移
    :param is_ocr:是否是二值图像匹配
    :return: max_val  最大匹配度
    """
    image_array = get_image(offset)
    result_list = []
    if is_ocr:
        # 将截图图像转为灰度图像
        gray_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        # 将灰度图像二值化，确保模板匹配是基于二值图像    只保留白色部分，其他的地方全变成黑的
        _, image_array = cv2.threshold(gray_array, 245, 255, cv2.THRESH_BINARY)
        # 读取模板图像
        for i in range(len(templates)):
            template = cv2.imread(templates[i], cv2.IMREAD_GRAYSCALE)
            # 执行模板匹配
            result = cv2.matchTemplate(image_array, template, cv2.TM_CCOEFF_NORMED)
            # 获取匹配结果中最大值的位置    min_val, max_val, min_loc, max_loc
            _, max_val, _, _ = cv2.minMaxLoc(result)
            result_list.append(max_val)
    else:
        # 以彩色模式读取图像。通常情况下，图像会以 BGR（蓝、绿、红）顺序的 NumPy 数组形式加载。
        for i in range(len(templates)):
            template = cv2.imread(templates[i], cv2.IMREAD_COLOR)
            # 执行模板匹配
            result = cv2.matchTemplate(image_array, template, cv2.TM_CCOEFF_NORMED)
            # 获取匹配结果中最大值的位置    min_val, max_val, min_loc, max_loc
            _, max_val, _, _ = cv2.minMaxLoc(result)
            result_list.append(max_val)

    return result_list[0] if len(result_list) == 1 else result_list


