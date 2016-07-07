import sys
import logging
import os

# логгирование
LOG_FILENAME = 'example.log'
os.remove(LOG_FILENAME)
logging.basicConfig(
    filename=LOG_FILENAME,
    format = '[%(asctime)s][%(levelname)s] %(message)s',
    level  = logging.INFO
)
logger = logging.getLogger("Life")
logger.info("Start programm")