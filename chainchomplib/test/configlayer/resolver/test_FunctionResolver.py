import os
import unittest

from parameterized import parameterized

from chainchomplib.configlayer.helperFunctions import get_local_host, get_date_time_now, get_host_name
from chainchomplib.configlayer.resolver.FunctionResolver import FunctionResolver
from chainchomplib.data import PathProvider


class FunctionResolverTest(unittest.TestCase):

    @parameterized.expand([
        ['{{get_local_host}}', get_local_host()],
        ['{{get_date_time_now}}', get_date_time_now()],
        ['{{get_host_name}}', get_host_name()],
    ])
    def test_that_it_resolves_base_functions(self, template_string, expected):
        result = FunctionResolver.resolve(template_string)
        assert result == expected

    @parameterized.expand([
        [f'{{{{read_file({os.path.join(os.path.join(PathProvider.base_config_folder(), "jinjaResolver"), "test.txt")})}}}}', 'testcontent'],
    ])
    def test_that_it_works_with_files(self, filename, expected):
        result = FunctionResolver.resolve(filename)
        assert result == expected

    @parameterized.expand([
        ['{{teststring', '{{teststring'],
        ['{{teststring}', '{{teststring}'],
        ['{teststring}', '{teststring}'],
        ['{teststring}}', '{teststring}}'],
        ['teststring}}', 'teststring}}'],
    ])
    def test_that_it_returns_the_string_itself_if_its_no_function_string(self, non_template_string, expected):
        result = FunctionResolver.resolve(non_template_string)
        assert result == expected

