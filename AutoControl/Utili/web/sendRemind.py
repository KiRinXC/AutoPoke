from urllib import request, parse
from datetime import datetime
import logging
from AutoControl.Utili.filesys.handler import Handler

def send_remind():
    """
    发送秒提醒
    """
    logger = logging.getLogger(__name__)
    handler = Handler()
    Settings = handler.download_json('Settings')
    # 再发喵提醒
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    time_now = f"{year}年{month}月{day}日 {hour}:{minute}"
    request.urlopen("http://miaotixing.com/trigger?" + parse.urlencode({"id": Settings['miao_code'], "text": time_now}))
    logger.info("---已发送喵提醒---")


