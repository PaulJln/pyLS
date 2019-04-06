import unittest
import os

from src.pyLS_pkg.classes.Directory import Directory
from src.pyLS_pkg.classes.ExplorerHelper import ExplorerHelper


class TestExplorerHelperMethods(unittest.TestCase):
    def setUp(self):
        self.directory = Directory('root', '.', False, False)

    def test_basic_search(self):
        ExplorerHelper.basic_search(self.directory)
        self.assertEqual(len(self.directory.get_directories()),
                         sum(os.path.isdir(i) for i in os.listdir(self.directory.get_path()) if i[0] != '.'))

    def test_hidden_search(self):
        ExplorerHelper.basic_search(self.directory)
        ExplorerHelper.hidden_search(self.directory)
        self.assertEqual(len(self.directory.get_directories()),
                         sum(os.path.isdir(i) for i in os.listdir(self.directory.get_path())) + 2)
