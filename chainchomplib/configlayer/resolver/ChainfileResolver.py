import os
import re
import yaml

from chainchomplib import LoggerInterface
from chainchomplib.configlayer.model.ChainfileModel import ChainfileModel

from chainchomplib.abstracts.AbstractResolver import AbstractResolver
from chainchomplib.configlayer.resolver.FunctionResolver import FunctionResolver
from chainchomplib.verify.SchemaVerifier import SchemaVerifier
from chainchomplib.verify.schema.ChainfileSchema import ChainfileSchema
from chainchomplib.exceptions.Exceptions import NotValidException


class ChainfileResolver(AbstractResolver):

    @staticmethod
    def resolve_config_file(path_to_file: str):

        if not os.path.isfile(path_to_file):
            return

        with open(path_to_file) as chainfile:
            try:
                chainfile_data = yaml.safe_load(chainfile)
            except yaml.YAMLError:
                LoggerInterface.error(f'The provided file is not in valid yaml syntax: {path_to_file}')
                return

        try:
            SchemaVerifier.verify(chainfile_data, ChainfileSchema())
        except NotValidException:
            return

        chainlink_sub_dict: dict = chainfile_data.get('chainlink')
        chainlink_name = chainlink_sub_dict.get('name')
        chainlink_next = chainlink_sub_dict.get('next')
        chainlink_previous = chainlink_sub_dict.get('previous')
        start = chainfile_data.get('start')
        stop = chainfile_data.get('stop')
        adapter_type = chainfile_data.get('adapter')
        profile = chainfile_data.get('profile')

        model = ChainfileModel(
            FunctionResolver.parse(chainfile_data['project']),
            FunctionResolver.parse(chainlink_name)
        )

        if chainlink_next is not None:
            model.next_link = [FunctionResolver.parse(link) for link in chainlink_next]

        if chainlink_previous is not None:
            model.previous_link = [FunctionResolver.parse(link) for link in chainlink_next]

        if start is not None:
            model.start = FunctionResolver.parse(start)

        if stop is not None:
            model.stop = FunctionResolver.parse(stop)

        if adapter_type is not None:
            model.adapter = FunctionResolver.parse(adapter_type)

        if profile is not None:
            model.profile = FunctionResolver.parse(profile)

        return model
