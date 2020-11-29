import os
import unittest

from parameterized import parameterized

from chainchomplib.configlayer.model.ChainfileModel import ChainfileModel
from chainchomplib.configlayer.resolver.ChainfileResolver import ChainfileResolver
from chainchomplib.data import PathProvider


class ChainfileResolverTest(unittest.TestCase):

    def setUp(self) -> None:
        self.configPath = os.path.join(PathProvider.base_config_folder(), 'chainfileResolver')

    def test_that_it_does_not_work_with_invalid_data(self):
        result = ChainfileResolver.resolve_config_file(os.path.join(self.configPath, 'invalid_data.yml'))
        assert result is None

    def test_that_it_does_not_work_on_non_yml_files(self):
        result = ChainfileResolver.resolve_config_file(os.path.join(self.configPath, 'invalid_yml_file.yml'))
        assert result is None

    def test_that_it_does_not_work_if_path_is_not_file(self):
        result = ChainfileResolver.resolve_config_file(self.configPath)
        assert result is None

    @parameterized.expand([
        ['minimal_chainfile.yml', ChainfileModel('test', 'test')],
        ['test_chainfile_1.yml', ChainfileModel('test', 'test', ['test', 'test2'])],
        ['test_chainfile_2.yml', ChainfileModel('test', 'test', ['test'], start='test')],
        ['test_chainfile_3.yml', ChainfileModel('test', 'test', ['test'], adapter='test', start='test')],
    ])
    def test_that_it_only_adds_existing_data_to_model(self, file, expected):
        result = ChainfileResolver.resolve_config_file(os.path.join(self.configPath, file))
        assert result == expected

