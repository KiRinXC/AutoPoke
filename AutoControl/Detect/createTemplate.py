import os
import cv2
from AutoControl.Utili.filesys.getRoot import get_root
from AutoControl.Detect.getImage import get_image
def create_template(save_path,offset,ocr):
    """
    生成模板
    :param save_path: 模板保存路径 xxx.png
    :param offset: 偏移
    :param ocr: 是否转换成二值图像
    :return:
    """
    root_path = get_root()
    save_path = os.path.join(root_path, 'template/'+save_path)
    image_array = get_image(offset)
    if ocr:
        # 将截图图像转为灰度图像
        gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        # 将灰度图像二值化，确保模板匹配是基于二值图像
        _, image_array = cv2.threshold(gray_image, 245, 255, cv2.THRESH_BINARY)
    cv2.imwrite(str(save_path), image_array)




