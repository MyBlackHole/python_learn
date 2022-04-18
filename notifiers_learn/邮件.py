import notifiers
from loguru import logger
from notifiers.logging import NotificationHandler

params = {
    "host": "smtp.qq.com",
    "port": 465,
    "username": "1358244533@qq.com",
    "from": "1358244533@qq.com",
    "password": "wettvkqaipkdfgdi",
    "to": ["myisblackhole@163.com"],
    "subject": "邮件标题",
    "ssl": True
    # "tls": True
}

# test send
# notifier = notifiers.get_notifier("email")
# notifier.notify(message="The application is running!", **params)

# Be alerted on each error message

handler = NotificationHandler("email", defaults=params)


def error_only(record):
    return record["level"].name == "ERROR"


logger.add(handler, filter=error_only)
# logger.add(handler)
logger.error("我来了")
