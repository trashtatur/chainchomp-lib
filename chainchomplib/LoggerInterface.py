import logging
import os

from chainchomplib.data import PathProvider

if 'CHAINCHOMP_TEST' not in os.environ or os.environ.get('CHAINCHOMP_TEST') is '0':
    logging.basicConfig(filename=os.path.join(PathProvider.log_folder(), 'info.log'), format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, filemode='w')
    logging.basicConfig(filename=os.path.join(PathProvider.log_folder(), 'debug.log'), format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG, filemode='w')
    logging.basicConfig(filename=os.path.join(PathProvider.log_folder(), 'warning.log'), format='%(asctime)s %(levelname)s:%(message)s', level=logging.WARNING, filemode='w')
    logging.basicConfig(filename=os.path.join(PathProvider.log_folder(), 'error.log'), format='%(asctime)s %(levelname)s:%(message)s', level=logging.ERROR, filemode='w')
    logging.basicConfig(filename=os.path.join(PathProvider.log_folder(), 'critical.log'), format='%(asctime)s %(levelname)s:%(message)s', level=logging.CRITICAL, filemode='w')

if 'CHAINCHOMP_TEST' in os.environ and os.environ.get('CHAINCHOMP_TEST') is '1':
    logging.disable(logging.CRITICAL)


def info(message: str):
    logging.info(message)


def debug(message: str):
    logging.debug(message)


def warning(message: str):
    logging.warning(message)


def error(message: str):
    logging.error(message)


def critical(message: str):
    logging.critical(message)