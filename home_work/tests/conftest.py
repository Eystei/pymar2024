from log_.logging_setup import setup_logging, get_logger


def pytest_addoption(parser):
    parser.addoption(
        "--custom-log-level",
        action="store",
        default="INFO",
        help="Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL, TEST, SUCCESS)"
    )


def pytest_configure(config):
    setup_logging()
    log_level = config.getoption("--custom-log-level")
    if log_level is None:
        log_level = 'INFO'
    logger = get_logger("pytest_logger")
    logger.setLevel(log_level.upper())


def pytest_runtest_setup(item):
    log_level = item.config.getoption("--log-level")
    logger = get_logger("pytest_logger")
    logger.info(f"Starting test {item.name} with log level {log_level}")
