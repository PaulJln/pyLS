from .classes.Directory import Directory
from .classes.File import File
from .classes.ExplorerHelper import ExplorerHelper
from .options import OPTION_MAP, get_dirs_and_files
from .display import display


def resolve_dir(directory, options_dic):
    get_dirs_and_files(directory)
    for key, value in options_dic.items():
        if value:
            OPTION_MAP[key](directory)
    if directory.recursive:
        for d in directory.get_directories():
            resolve_dir(d, options_dic)


def split_dirs_files(paths):
    d = dict()
    d["files"] = []
    d["dirs"] = []

    for p in paths:
        if not ExplorerHelper.is_directory(p):
            if not ExplorerHelper.is_file(p):
                print("CANT ACCESS TO THIS DIRECTORY : " + p)
                continue
            d["files"].append(p)
            continue
        d["dirs"].append(p)

    return d


def manage_directories(directories, options_dic, recursive, reverse):
    dir_list = []

    for d in directories:
        directory = Directory('', d, recursive, reverse)
        resolve_dir(directory, options_dic)
        dir_list.append(directory)

    return dir_list


def manage_options(options_dic, paths, recursive, reverse):
    if not paths:
        paths.append('.')
    paths = split_dirs_files(paths)
    if reverse:
        paths["files"].reverse()
        paths["dirs"].reverse()
    files = manage_files(paths["files"], options_dic)
    directories = manage_directories(paths["dirs"], options_dic, recursive, reverse)
    display(files, directories)


def manage_files(files, options_dic):
    file_list = []

    for f in files:
        file = File(f, f)
        for key, value in options_dic.items():
            if value:
                OPTION_MAP[key](file)
        file_list.append(file)

    return file_list


