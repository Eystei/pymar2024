from enum import Enum


class AnsiColorCode(Enum):
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD_BRIGHT_RED = '\033[1;91m'
    BOLD_BRIGHT_GREEN = '\033[1;92m'
    BOLD_BRIGHT_YELLOW = '\033[1;93m'
    BOLD_BRIGHT_BLUE = '\033[1;94m'
    BOLD_BRIGHT_MAGENTA = '\033[95m'
    BOLD_BRIGHT_CYAN = '\033[1;96m'
    BOLD_BRIGHT_WHITE = '\033[1;97m'

    def __str__(self) -> str:
        return self.value
