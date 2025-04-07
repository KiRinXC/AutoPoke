import logging
import os
from logging.handlers import TimedRotatingFileHandler
from AutoControl.Utili.filesys.handler import Handler

def setup_logging():
    # 先确定日志文件的地址
    handler = Handler()
    Settings = handler.download_json("Settings")
    is_debug = Settings["is_debug"]
    log_dir = handler.log_dir
    log_file = os.path.join(log_dir, 'AutoPoke.log')
    # 创建一个全局日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # 设置全局日志级别

    # 日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 文件日志处理器（按天切割）,只保留七个
    file_handler = TimedRotatingFileHandler(
        log_file, when='midnight', interval=1, backupCount=7, encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    file_handler.suffix = "%Y-%m-%d.log"  # 设置日志文件名格式
    logger.addHandler(file_handler)

    # 控制台日志处理器
    if is_debug==1:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    return logger