import random
import logging
log  = logging.getLogger(__name__)
from AutoControl.Utili.filesys.handler import Handler
handler = Handler()
Settings = handler.download_json("Settings")
# - 高概率的短时间分布（概率0.99）
# - 中概率的平均分布（概率0.009）
# - 低概率的平均分布（概率0.001）
high_prob=Settings["high_prob"]
mid_prob=Settings["mid_prob"]
low_prob=Settings["low_prob"]

def gen_1d_uniform(scope):
    """
    生成一维均匀分布
    :param scope: 生成数据的范围[x,y]
    """
    return random.uniform(scope[0], scope[1])

def gen_2d_uniform(region):
    """
    主要用于生成点击的坐标
    :param region:
    """
    x, y, width, height = region
    loc_x = gen_1d_uniform([x, x + width])
    loc_y = gen_1d_uniform([y, y + height])
    return loc_x, loc_y

def gen_1d_accident(scope, item = None):
    """
    生成包含事故的一维分布：
    :param scope: 正常一维分布的范围，格式为 [min, max]
    :param item: 调用此函数的事件
    """
    pro = random.random()
    if pro <= high_prob:
        result = gen_1d_uniform(scope)
        log.debug(f"{item}事件触发极短阻塞,时长{result}")
    elif pro <= high_prob+mid_prob:
        result = gen_1d_uniform([scope[1], 10])
        log.info(f"{item}事件触发短时间挂机,时长{result}")
    else:
        result = gen_1d_uniform([10,90])
        log.error(f"{item}事件触发长时间挂机,时长{result}")
    return result