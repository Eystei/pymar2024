import json
import logging
import logging.config
import os

from .colored_formatter import ColoredFormatter
from .additional_func import add_logging_level

add_logging_level('TEST', 25)
add_logging_level('SUCCESS', 26)

logging_initialized = False


def setup_logging():
    global logging_initialized
    if not logging_initialized:
        log_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        directory = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(directory, 'logging.conf')
        with open(path, 'r') as f:
            config = json.load(f)
        config['formatters']['colored']['()'] = ColoredFormatter

        for handler in config['handlers'].values():
            if 'filename' in handler:
                handler['filename'] = os.path.join(
                    log_directory,
                    os.path.basename(handler['filename']))

        logging.config.dictConfig(config)
        logging_initialized = True


def get_logger(name):
    global logging_initialized
    if not logging_initialized:
        setup_logging()
    return logging.getLogger(name)
