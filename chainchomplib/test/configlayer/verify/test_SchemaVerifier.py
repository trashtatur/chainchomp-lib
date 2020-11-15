import unittest

from chainchomplib.configlayer.verify.SchemaVerifier import SchemaVerifier
from chainchomplib.exceptions.Exceptions import NotValidException
from parameterized import parameterized

from chainchomplib.configlayer.verify.schema.ChainfileSchema import ChainfileSchema


class SchemaVerifierTest(unittest.TestCase):

    @parameterized.expand([
        [{}, ChainfileSchema(), NotValidException],
        [{'project': 'test'}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'start': 'test'}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'start': 'test', 'stop': 'test'}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'start': 'test', 'stop': 'test', 'profile': 'test'}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'start': 'test', 'stop': 'test', 'profile': 'test', 'adapter': 'test'}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'chainlink': 'test'}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'chainlink': {'next': 'test'}}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'chainlink': {'previous': 'test'}}, ChainfileSchema(), NotValidException],
        [{'project': 'test', 'chainlink': {'next': 'test', 'previous': 'test'}}, ChainfileSchema(), NotValidException],
        [{'chainlink': {'next': 'test', 'previous': 'test'}}, ChainfileSchema(), NotValidException],
        [{'chainlink': {'name': 'test', 'next': 'test', 'previous': 'test'}}, ChainfileSchema(), NotValidException],
    ])
    def test_that_an_exception_is_thrown_on_invalid_data(self, data, schema, exception):
        with self.assertRaises(exception):
            SchemaVerifier.verify(data, schema)

    @parameterized.expand([
        [{'project': 'test', 'chainlink': {'name': 'test', 'next': 'test'}}, ChainfileSchema()],
        [{'project': 'test', 'chainlink': {'name': 'test', 'next': 'test', 'previous': 'test'}}, ChainfileSchema()],
        [{'project': 'test', 'chainlink': {'name': 'test'}}, ChainfileSchema()],
        [{'project': 'test', 'chainlink': {'name': 'test'}, 'start': 'test'}, ChainfileSchema()],
        [{'project': 'test', 'chainlink': {'name': 'test'}, 'start': 'test', 'stop': 'test'}, ChainfileSchema()],
        [{'project': 'test', 'chainlink': {'name': 'test'}, 'start': 'test', 'stop': 'test', 'profile': 'test'}, ChainfileSchema()],
        [{'project': 'test', 'chainlink': {'name': 'test'}, 'start': 'test', 'stop': 'test', 'profile': 'test', 'adapter': 'test'}, ChainfileSchema()],
    ])
    def test_that_correct_data_is_accepted(self, data, schema):
        result = SchemaVerifier.verify(data, schema)
        assert result == data
