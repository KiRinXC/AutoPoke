from datetime import datetime
def duration(initial_time):
    """
    解析密钥中的起始日期，计算时长，返回天数
    :return: 天数
    """
    # 初始时间字符串
    initial_time = datetime.strptime(initial_time, "%Y%m%d")
    # 获取当前时间
    current_time = datetime.now()
    # 计算时间差
    time_difference = current_time - initial_time
    # 获取相差的天数
    days_difference = time_difference.days

    return days_difference