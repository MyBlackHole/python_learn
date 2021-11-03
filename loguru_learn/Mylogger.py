import logging


fmt = '%(asctime)s - %(thread)d - %(process)d - %(funcName)s - %(module)s - %(lineno)d - %(levelname)s - [%(message)s]'

def new_logger(name, log_path='info.log', level=logging.DEBUG, handler_level=logging.DEBUG, console_level=logging.DEBUG, handler_fmt=fmt, console_fmt=fmt):
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


logger = new_logger(__name__)
logger.debug('ok')
logger.info('ok')
