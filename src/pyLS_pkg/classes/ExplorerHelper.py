import os
from os import walk
from .Directory import Directory
from .File import File

CODEC_ISO = "ISO-8859-1"


class ExplorerHelper:
    @staticmethod
    def basic_search(instance):
        path = instance.get_path()

        for (dirPath, dirNames, fileNames) in walk(path):
            for f in fileNames:
                if not f[0] == '.':
                    instance.add_file(File(f, path + '/' + f))
            for d in dirNames:
                if not d[0] == '.':
                    instance.add_directory(Directory(d, path + '/' + d, instance.recursive, instance.reverse))
            break

    @staticmethod
    def hidden_search(instance):
        path = instance.get_path()

        if path:
            if type(instance) is Directory:
                instance.add_directory(Directory('.', '', False, instance.reverse))
                instance.add_directory(Directory('..', '', False, instance.reverse))
            for (dirPath, dirNames, fileNames) in os.walk(path):
                for f in fileNames:
                    if f[0] == '.':
                        instance.add_file(File(f, path + '/' + f))
                for d in dirNames:
                    if d[0] == '.':
                        instance.add_directory(Directory(d, path + '/' + d, instance.recursive, instance.reverse))
                break

    @staticmethod
    def get_size(instance):
        if type(instance) is File:
            instance.set_size(os.path.getsize(instance.get_path()))
        else:
            for f in instance.get_files():
                f.set_size(os.path.getsize(f.get_path()))
            for d in instance.get_directories():
                d.set_size(os.path.getsize(d.get_path()))

    @staticmethod
    def get_nb_lines(file):
        file.set_nb_lines(sum(1 for line in open(file.get_path(), encoding=CODEC_ISO)))

    @staticmethod
    def get_nb_files_in_dir(directory):
        for d in directory.get_directories():
            if d.get_path() is not '':
                d.set_nb_files(
                    len([name for name in os.listdir(d.get_path()) if
                         os.path.isfile(os.path.join(d.get_path(), name))]))

    @staticmethod
    def is_directory(path):
        return os.path.isdir(path)

    @staticmethod
    def is_file(path):
        return os.path.isfile(path)
