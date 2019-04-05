import os
from os import walk
from .utils import Directory, File


class ExplorerHelper:
    @staticmethod
    def basic_search(directory):
        path = directory.get_name()
        if not os.path.exists(path):
            print('ERROR FILE OR DIRECTORY DOES NOT EXIST')

        if os.path.isfile(path):
            directory.add_file(File(path))
            return

        for (dirPath, dirNames, fileNames) in walk(path):
            for f in fileNames:
                if not f[0] == '.':
                    directory.add_file(File(f))
            for d in dirNames:
                if not d[0] == '.':
                    directory.add_directory(Directory(d, directory.recursive, directory.reverse))
            break

    @staticmethod
    def hidden_search(directory):
        if not os.path.exists(directory.get_name()):
            print('ERROR FILE OR DIRECTORY DOES NOT EXIST')
        for (dirPath, dirNames, fileNames) in walk(directory.get_name()):
            for f in fileNames:
                if f[0] == '.':
                    directory.add_file(File(f))
            for d in dirNames:
                if d[0] == '.':
                    directory.add_directory(Directory(d, directory.recursive, directory.reverse))

    @staticmethod
    def get_size(directory):
        for f in directory.get_files():
            f.set_size(os.path.getsize(f.get_name()))
        for d in directory.get_directories():
            d.set_size(os.path.getsize(d.get_name()))

    @staticmethod
    def get_files_nb_lines(directory):
        for f in directory.get_files():
            f.set_nb_lines(sum(1 for line in open(f.get_name())))

    @staticmethod
    def get_nb_files(directory):
        for d in directory.get_directories():
            d.set_nb_files(
                len([name for name in os.listdir(d.get_name()) if os.path.isfile(os.path.join(d.get_name(), name))]))