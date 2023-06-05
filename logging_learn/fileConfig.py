import logging.config

logging.config.fileConfig(fname='file.ini', disable_existing_loggers=False)
logger = logging.getLogger("sampleLogger")
# 省略日志输出
