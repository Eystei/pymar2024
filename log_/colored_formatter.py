import logging

from log_.color_codes_enum import AnsiColorCode


class ColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': AnsiColorCode.BOLD_BRIGHT_BLUE,
        'INFO': AnsiColorCode.BOLD_BRIGHT_WHITE,
        'WARNING': AnsiColorCode.BOLD_BRIGHT_YELLOW,
        'ERROR': AnsiColorCode.BOLD_BRIGHT_RED,
        'CRITICAL': AnsiColorCode.BOLD_BRIGHT_RED,
        'TEST': AnsiColorCode.BOLD_BRIGHT_CYAN,
        'SUCCESS': AnsiColorCode.BOLD_BRIGHT_GREEN
    }
    RESET = '\033[0m'

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        message = super().format(record)
        return f"{log_color}{message}{self.RESET}"
