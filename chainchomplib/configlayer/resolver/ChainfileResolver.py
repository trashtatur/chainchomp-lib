import os
import yaml
from chainchomplib.configlayer.model.ChainlinkConfigModel import ChainlinkConfigModel

from chainchomplib.abstracts.AbstractResolver import AbstractResolver
from chainchomplib.configlayer.verify.SchemaVerifier import SchemaVerifier
from chainchomplib.configlayer.verify.schema.ChainfileSchema import ChainfileSchema


class ChainfileResolver(AbstractResolver):

    def resolve_config_file(self, path_to_file: str):

        if not os.path.isfile(path_to_file):
            return

        chainfile_data = None
        with open(path_to_file) as chainfile:
            try:
                chainfile_data = yaml.safe_load(chainfile)
            except yaml.YAMLError:
                # TODO handle Exception
                print('Failed to load chainfile')

        schema_is_valid = SchemaVerifier.verify(chainfile_data, ChainfileSchema().schema)

        if not schema_is_valid:
            return

        chainlink_sub_dict: dict = chainfile_data.get('chainlink')
        chainlink_name = chainlink_sub_dict.get('name')
        chainlink_next = chainlink_sub_dict.get('next')
        chainlink_previous = chainlink_sub_dict.get('previous')
        start = chainlink_sub_dict.get('start')
        stop = chainlink_sub_dict.get('stop')
        adapter_type = chainlink_sub_dict.get('mqtype')
        profile = chainlink_sub_dict.get('profile')

        model = ChainlinkConfigModel(
            chainfile_data['project'],
            chainlink_name
        )

        if chainlink_next is not None:
            model.next_link = chainlink_next

        if chainlink_previous is not None:
            model.previous_link = chainlink_previous

        if start is not None:
            model.start = start

        if stop is not None:
            model.stop = stop

        if adapter_type is not None:
            model.mq_type = adapter_type

        if profile is not None:
            model.profile = profile

        return model
