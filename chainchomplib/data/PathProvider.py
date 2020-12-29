import os
from pathlib import Path


def env_based_base_folder():
    if 'CHAINCHOMP_TEST' not in os.environ:
        return Path.home()

    if os.environ.get('CHAINCHOMP_TEST') is '0':
        return Path.home()

    if os.environ.get('CHAINCHOMP_TEST') is '1':
        if 'CHAINCHOMP_TEST_DIR' not in os.environ:
            return Path.home()

        return Path(os.environ.get('CHAINCHOMP_TEST_DIR'))


def base_config_folder():
    path = env_based_base_folder()
    return path.joinpath('.chainchomp')


def projects_folder():
    return base_config_folder().joinpath('projects')


def profiles_folder():
    return base_config_folder().joinpath('profiles')


def env_var_folder():
    return base_config_folder().joinpath('envvars')


def installed_adapters_folder():
    return base_config_folder().joinpath('adapters')


def fixtures_folder():
    return base_config_folder().joinpath('fixtures')


def log_folder():
    return base_config_folder().joinpath('logs')


def chainlinks_folder():
    return base_config_folder().joinpath('chainlinks')

