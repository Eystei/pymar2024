import logging
import logging.config
from datetime import datetime
import os
import json


class LoggerSets:
    @staticmethod
    def setup_logging_test():
        config_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'test_logging.conf')

        with open(config_path, 'r') as file:
            log_config = json.load(file)

        log_dir = os.path.join(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))), '_artifacts/_logs')
        os.makedirs(log_dir, exist_ok=True)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_file = os.path.join(log_dir, f'test_{current_time}.log')

        log_config['handlers']['file']['filename'] = log_file
        logging.config.dictConfig(log_config)

    @staticmethod
    def setup_reports_test(config):
        report_dir = os.path.join(os.path.dirname(os.path.dirname(
            os.path.abspath(__file__))), '_artifacts/_reports')
        os.makedirs(report_dir, exist_ok=True)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        html_report_path = os.path.join(report_dir, f'test_report_{current_time}.html')
        config.option.htmlpath = html_report_path
