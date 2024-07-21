import pytest

from _logger.setup_methods import LoggerSets

"""
pytest tests -v --log-cli-level=DEBUG --log-file-level=DEBUG -q
"""


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    LoggerSets.setup_logging_test()
    LoggerSets.setup_reports_test(config)
