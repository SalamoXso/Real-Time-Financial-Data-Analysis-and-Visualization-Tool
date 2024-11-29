import logging
from config.config import config

# Set up logger
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = logging.FileHandler(config.get('LOG_FILE', 'app.log'))
log_handler.setFormatter(log_formatter)
log_handler.setLevel(logging.INFO)

logger = logging.getLogger('my_logger')
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

def write_log(message, level='INFO'):
    if level == 'INFO':
        logger.info(message)
    elif level == 'ERROR':
        logger.error(message)
    elif level == 'WARNING':
        logger.warning(message)
    elif level == 'DEBUG':
        logger.debug(message)
