from pathlib import Path


def base_config_folder():
    path = Path.home()
    return path.joinpath('.chainchomp')


def projects_folder():
    return base_config_folder().joinpath('projects')


def profiles_folder():
    return base_config_folder().joinpath('profiles')


def env_var_folder():
    return base_config_folder().joinpath('envvars')

