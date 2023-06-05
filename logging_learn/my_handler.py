import logging
import logging.config


class MyLogHandler(logging.Handler, object):
    """
    自定义日志handler
    """

    def __init__(self, name, other_attr=None, **kwargs):
        logging.Handler.__init__(self)
        print("初始化自定义日志处理器：", name)
        print("其它属性值：", other_attr)

    def emit(self, record):
        """
        emit函数为自定义handler类时必重写的函数，这里可以根据需要对日志消息做一些处理，比如发送日志到服务器

        发出记录(Emit a record)
        """
        try:
            msg = self.format(record)
            print("获取到的消息为：", msg)
            for item in dir(record):
                if item in ["process", "processName", "thread", "threadName"]:
                    print(item, "：", getattr(record, item))
            print("ok")
        except Exception:
            self.handleError(record)


# 测试
logging.basicConfig()
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
my_log_handler = MyLogHandler("LoggerHandler")
logger.addHandler(my_log_handler)
logger.info("hello，shouke")


# 运行handler.py，结果输出如下
# 初始化自定义日志处理器： LoggerHandler
# 其它属性值： None
# 获取到的消息为： hello，shouke
# process ： 27932
# processName ： MainProcess
# thread ： 45464
# threadName ： MainThread
# INFO:logger:hello，shouke
