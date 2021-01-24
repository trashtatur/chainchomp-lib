import os

import yaml
from chainchomplib.abstracts.AbstractResolver import AbstractResolver

from chainchomplib.exceptions.Exceptions import NotValidException
from chainchomplib.verify.SchemaVerifier import SchemaVerifier
from chainchomplib import LoggerInterface
from chainchomplib.configlayer.model.AdapterFileModel import AdapterFileModel
from chainchomplib.data import PathProvider
from chainchomplib.verify.schema.AdapterFileSchema import AdapterFileSchema


class AdapterResolver(AbstractResolver):

    @staticmethod
    def resolve(name: str) -> AdapterFileModel or None:
        path = os.path.join(PathProvider.installed_adapters_folder(), f'{name}.yml')
        if not os.path.isfile(path):
            return None

        with open(path, 'r') as adapter_file:
            try:
                data = yaml.safe_load(adapter_file)
            except yaml.YAMLError as error:
                LoggerInterface.error(f'Could not load adapter file with exception: {error}')
                return None
            else:
                try:
                    SchemaVerifier.verify(data, AdapterFileSchema())
                except NotValidException as error:
                    LoggerInterface.error(f'Loaded data is incorrect: {error}')
                    return None
                else:
                    return AdapterFileModel(
                        data.get('name'),
                        data.get('path'),
                        data.get('start'),
                        data.get('stop')
                    )
            finally:
                adapter_file.close()

