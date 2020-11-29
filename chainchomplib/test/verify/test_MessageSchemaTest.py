import unittest

from chainchomplib.exceptions.Exceptions import NotValidException
from parameterized import parameterized

from chainchomplib.verify.SchemaVerifier import SchemaVerifier
from chainchomplib.verify.schema.MessageSchema import MessageSchema


class MessageSchemaTest(unittest.TestCase):
    @parameterized.expand([
        [{'message_body': 'nothing', 'message_header': {'origin': 'A', 'recipients': ['B', 'C'], 'adapter_name': 'test'}}, MessageSchema()],
        [{'message_body': 'nothing', 'message_header': {'origin': 'A', 'recipients': ['B'], 'adapter_name': 'test'}}, MessageSchema()],
    ])
    def test_that_correct_data_is_accepted(self, data, schema):
        result = SchemaVerifier.verify(data, schema)
        assert result == data

    @parameterized.expand([
        [{'message_body': 'nothing', 'message_header': {'origin': 'A', 'recipients': ['B', 'C'], 'adapter_name': 200}}, MessageSchema(), NotValidException],
        [{'message_body': 'nothing', 'message_header': {'origin': 'A', 'recipients': [2, 'C'], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_body': 'nothing', 'message_header': {'origin': 'A', 'recipients': ['B', 2], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_body': 'nothing', 'message_header': {'origin': 400, 'recipients': ['B', 'C'], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_body': 33, 'message_header': {'origin': 'A', 'recipients': ['B', 'C'], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_booty': 'nothing', 'message_header': {'origin': 'A', 'recipients': ['B', 'C'], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_body': 'nothing', 'message_head': {'origin': 'A', 'recipients': ['B', 'C'], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_body': 'nothing', 'message_header': {'originator': 'A', 'recipients': ['B', 'C'], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_body': 'nothing', 'message_header': {'origin': 'A', 'recipientator': ['B', 'C'], 'adapter_name': 'test'}}, MessageSchema(), NotValidException],
        [{'message_body': 33, 'message_header': {'origin': 'A', 'recipients': ['B', 'C'], 'adapter_nomnomnom': 'test'}}, MessageSchema(), NotValidException],
    ])
    def test_that_an_exception_is_thrown_on_invalid_data(self, data, schema, exception):
        with self.assertRaises(exception):
            SchemaVerifier.verify(data, schema)


if __name__ == '__main__':
    unittest.main()
