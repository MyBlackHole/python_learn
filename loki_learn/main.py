import logging

from nextlog import Logger

# Define labels for logs
labels = {'source': 'localhost'}

# Loki server URL
loki_url = "http://localhost:3100/api/prom/push"

# Initialize nextlog logger
logger = Logger(__name__,  loki_url=loki_url, labels=labels)

# Apply preferred logging configs
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler('console2.log')
logger.addHandler(file_handler)

# Log messages
logger.error("Error log 1")
logger.error("Error log 2")
logger.critical("Critical log 1")
logger.critical("Critical log 2")
logger.error("Error log 3")
