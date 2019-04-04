import os
from os import walk
from typing import List
from utils import Directory, File


def all_option(files, directories, path):
    for (dirPath, dirNames, fileNames) in walk(path):
        for f in fileNames:
            if f[0] == '.':
                files.append(File(f))
        for d in dirNames:
            if d[0] == '.':
                directories.append(Directory(d))
        break

    print('this is count')


def recursive_option(files, directories, path):
    print('this is recursive')


def long_option(files, directories, path):
    for f in files:
        f.set_size(os.path.getsize(f.get_name()))
    for d in directories:
        d.set_size(os.path.getsize(d.get_name()))


def count_option(files, directories, path):
    for f in files:
        f.set_nb_lines(sum(1 for line in open(f.get_name())))


def directory_option(files, directories, path):
    files.clear()
    for d in directories:
        d.set_nb_files(
            len([name for name in os.listdir(d.get_name()) if os.path.isfile(os.path.join(d.get_name(), name))]))


def reverse_option(files, directories, path):
    print('this is reverse')


def get_dirs_and_files(files, directories, path):
    if not os.path.exists(path):
        print('ERROR FILE OR DIRECTORY DOES NOT EXIST')

    if os.path.isfile(path):
        return files.append(File(path))

    for (dirPath, dirNames, fileNames) in walk(path):
        for f in fileNames:
            if not f[0] == '.':
                files.append(File(f))
        for d in dirNames:
            if not d[0] == '.':
                directories.append(Directory(d))
        break


def manage_options(args_dic, paths):
    files = []
    directories = []

    if not paths:
        paths = '.'
    for path in paths:
        get_dirs_and_files(files, directories, path)
        for key, value in args_dic.items():
            if key != 'paths' and value:
                OPTION_MAP[key](files, directories, path)

    for f in files:
        print(f.get_name() + ' ' + str(f.get_size()) + ' ' + str(f.get_nb_lines()))
    for d in directories:
        print(d.get_name() + ' ' + str(d.get_size()) + ' ' + str(d.get_nb_files()))


OPTION_MAP = {
    'all': all_option,
    'Recursive': recursive_option,
    'long': long_option,
    'count': count_option,
    'directory': directory_option,
    'reverse': reverse_option
}
