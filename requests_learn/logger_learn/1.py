import logging

fmt = '%(asctime)s - %(thread)d - %(process)d - %(funcName)s - %(module)s - %(lineno)d - %(levelname)s - [%(message)s]'

def new_logger(name, log_path='info.log', level=logging.INFO, handler_level=logging.INFO, console_level=logging.NOTSET, handler_fmt=fmt, console_fmt=fmt):
    logger = logging.getLogger(name=name)
    logger.setLevel(level=level)

    handler = logging.FileHandler(log_path)
    handler.setLevel(level=handler_level)
    handler.setFormatter(logging.Formatter(fmt=handler_fmt))

    console = logging.StreamHandler()
    console.setLevel(level=console_level)
    console.setFormatter(logging.Formatter(fmt=console_fmt))

    logger.addHandler(handler)
    logger.addHandler(console)
    return logger


logger = new_logger(name=__name__)
logger2 = new_logger(name="abc", log_path="text.log")

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")

logger2.info("Start print log")
logger2.debug("Do something")
logger2.warning("Something maybe fail.")
logger2.info("Finish")
