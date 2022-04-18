# from log import logger
from loguru import logger

logger.info("")
logger.warning("1")


# @logger.catch
# def t():
#     try:
#         assert 1 > 2
#     except:
#         pass
#
#
# t()
try:
    i = 1 / 0
except Exception as e:
    logger.exception(e)
