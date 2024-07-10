import logging


# ------------------------------------ part 3 ------------------------------------
# logging.basicConfig(filename='./logs/app.log', filemode='a',
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')
# ------------------------------------ part 3 ------------------------------------


# ------------------------------------ part 4 ------------------------------------
# logger = logging.getLogger('my_logger')
# logger2 = logging.getLogger('my_logger2')
#
# logger.setLevel(logging.DEBUG)
# logger2.setLevel(logging.WARNING)
#
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
#
# logger.addHandler(ch)
# logger.debug('This is a debug message')
# logger.warning('This is a warning message')
#
# logger2.debug('This is a debug message by logger 2')
# logger2.warning('This is a warning message by logger 2')
# ------------------------------------ part 4 ------------------------------------


# ------------------------------------ part 5 ------------------------------------
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('my_logger')
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

logger.debug('This is a sample debug message')
# ------------------------------------ part 5 ------------------------------------
