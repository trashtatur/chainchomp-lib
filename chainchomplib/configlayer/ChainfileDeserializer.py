from chainchomplib.configlayer.resolver.FunctionResolver import FunctionResolver

from chainchomplib.exceptions.Exceptions import NotValidException

from chainchomplib.configlayer.model.ChainfileModel import ChainfileModel

from chainchomplib.verify.schema.ChainfileSchema import ChainfileSchema

from chainchomplib.verify.SchemaVerifier import SchemaVerifier


class ChainfileDeserializer:

    @staticmethod
    def deserialize(data: dict) -> ChainfileModel or None:
        try:
            SchemaVerifier.verify(data, ChainfileSchema())
        except NotValidException:
            return None
        else:
            chainlink_sub_dict: dict = data.get('chainlink')
            chainlink_name = chainlink_sub_dict.get('name')
            chainlink_next = chainlink_sub_dict.get('next', None)
            chainlink_previous = chainlink_sub_dict.get('previous', None)
            start = data.get('start', None)
            stop = data.get('stop', None)
            adapter_type = data.get('adapter', None)
            profile = data.get('profile', None)

            model = ChainfileModel(
                FunctionResolver.resolve(data['project']),
                FunctionResolver.resolve(chainlink_name)
            )

            if chainlink_next is not None:
                model.next_links = [FunctionResolver.resolve(link) for link in chainlink_next]

            if chainlink_previous is not None:
                model.previous_links = [FunctionResolver.resolve(link) for link in chainlink_next]

            if start is not None:
                model.start = FunctionResolver.resolve(start)

            if stop is not None:
                model.stop = FunctionResolver.resolve(stop)

            if adapter_type is not None:
                model.adapter = FunctionResolver.resolve(adapter_type)

            if profile is not None:
                model.profile = FunctionResolver.resolve(profile)

            return model
