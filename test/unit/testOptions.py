import unittest
import os

from src.pyLS_pkg.classes.Directory import Directory
from src.pyLS_pkg.options import get_dirs_and_files, directory_option, all_option


class TestOptions(unittest.TestCase):
    def setUp(self):
        self.directory = Directory('root', '.', False, False)

    def test_all_option(self):
        get_dirs_and_files(self.directory)
        all_option(self.directory)
        self.assertEqual(len(self.directory.get_directories()),
                         sum(os.path.isdir(i) for i in os.listdir(self.directory.get_path())) + 2)

    def test_directory_option(self):
        get_dirs_and_files(self.directory)
        directory_option(self.directory)
        self.assertEqual(0, len(self.directory.get_files()))
