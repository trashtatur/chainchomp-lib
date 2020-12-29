import os
import socket
from datetime import date

from chainchomplib import LoggerInterface


def get_local_host() -> str:
    return socket.gethostbyname(get_host_name())


def get_date_time_now() -> str:
    return date.today().strftime('%Y-%m-%d')


def get_host_name() -> str:
    return socket.gethostname()


def read_file(path: str) -> str:
    if not os.path.isfile(path):
        LoggerInterface.critical(f'The provided path {path} is not a file. It wont be parsed')
        return path

    with open(path, 'r') as file:
        try:
            return file.read()
        finally:
            file.close()

