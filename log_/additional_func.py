import logging


def add_logging_level(level_name, level_num):

    def log_for_level(self, message, *args, **kwargs):
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs, stacklevel=2)

    logging.addLevelName(level_num, level_name)
    setattr(logging.Logger, level_name.lower(), log_for_level)
