import os
from os import walk


def all_option(files, directories, information, path):
    print('all directories')


def recursive_option(information, path):
    print('this is recursive')


def long_option(information, path):
    print('this is long')


def count_option(information, path):
    print('this is count')


def directory_option(information, path):
    print('this is directory ' + path)


def reverse_option(information, path):
    print('this is reverse')


def get_dirs_and_files(path):
    files = []
    directories = []

    if not os.path.exists(path):
        print('ERROR FILE OR DIRECTORY DOES NOT EXIST')

    if os.path.isfile(path):
        return path

    for (dirPath, dirNames, fileNames) in walk(path):
        files.extend([f for f in fileNames if not f[0] == '.'])
        directories.extend([d for d in dirNames if not d[0] == '.'])
        break

    return [files, directories]


def manage_options(args_dic, paths):
    if not paths:
        paths = '.'

    for path in paths:
        print(get_dirs_and_files(path))
        information = []
        for key, value in args_dic.items():
            if key != 'paths' and value:
                OPTION_MAP[key](information, path)


OPTION_MAP = {
    'all': all_option,
    'Recursive': recursive_option,
    'long': long_option,
    'count': count_option,
    'directory': directory_option,
    'reverse': reverse_option
}
