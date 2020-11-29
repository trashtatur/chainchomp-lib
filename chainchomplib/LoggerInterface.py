import logging
import os

from chainchomplib.data import PathProvider

_logger = logging.getLogger('chainchomp')

if 'CHAINCHOMP_TEST' not in os.environ or os.environ.get('CHAINCHOMP_TEST') is '0':
    """
    Set formatter
    """
    formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s: %(message)s')

    """
    Set proper file handlers for logging
    """
    file_handler_info = logging.FileHandler(os.path.join(PathProvider.log_folder(), 'info.log'))
    file_handler_info.setLevel(logging.INFO)
    file_handler_info.setFormatter(formatter)
    _logger.addHandler(file_handler_info)

    file_handler_debug = logging.FileHandler(os.path.join(PathProvider.log_folder(), 'debug.log'))
    file_handler_debug.setLevel(logging.DEBUG)
    file_handler_debug.setFormatter(formatter)
    _logger.addHandler(file_handler_debug)

    file_handler_warning = logging.FileHandler(os.path.join(PathProvider.log_folder(), 'warning.log'))
    file_handler_warning.setLevel(logging.WARNING)
    file_handler_warning.setFormatter(formatter)
    _logger.addHandler(file_handler_warning)

    file_handler_error = logging.FileHandler(os.path.join(PathProvider.log_folder(), 'error.log'))
    file_handler_error.setLevel(logging.ERROR)
    file_handler_error.setFormatter(formatter)
    _logger.addHandler(file_handler_error)

    file_handler_critical = logging.FileHandler(os.path.join(PathProvider.log_folder(), 'critical.log'))
    file_handler_critical.setLevel(logging.CRITICAL)
    file_handler_critical.setFormatter(formatter)
    _logger.addHandler(file_handler_critical)

    """
    Set console handlers for higher log levels
    """
    console_error_handler = logging.StreamHandler()
    console_error_handler.setLevel(logging.ERROR)
    console_error_handler.setFormatter(formatter)
    _logger.addHandler(console_error_handler)

    console_critical_handler = logging.StreamHandler()
    console_critical_handler.setLevel(logging.CRITICAL)
    console_critical_handler.setFormatter(formatter)
    _logger.addHandler(console_critical_handler)

if 'CHAINCHOMP_TEST' in os.environ and os.environ.get('CHAINCHOMP_TEST') is '1':
    logging.disable(logging.CRITICAL)


def info(message: str):
    _logger.info(message)


def debug(message: str):
    _logger.debug(message)


def warning(message: str):
    _logger.warning(message)


def error(message: str):
    _logger.error(message)


def critical(message: str):
    _logger.critical(message)
