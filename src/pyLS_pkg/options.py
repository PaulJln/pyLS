from .utils import Directory, File
from .ExplorerHelper import ExplorerHelper


def get_dirs_and_files(instance):
    ExplorerHelper.basic_search(instance)


def all_option(instance):
    ExplorerHelper.hidden_search(instance)


def long_option(instance):
    ExplorerHelper.get_size(instance)


def count_option(instance):
    if type(instance) is File:
        ExplorerHelper.get_nb_lines(instance)
    else:
        for f in instance.get_files():
            ExplorerHelper.get_nb_lines(f)


def directory_option(instance):
    if type(instance) is Directory:
        instance.clear_files()
        ExplorerHelper.get_nb_files_in_dir(instance)


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


def display_dir(directory, display_name_dir):
    directories = directory.get_directories()
    directories.sort(key=lambda inst: inst.get_name().strip('.'))
    if display_name_dir or directory.recursive:
        print(directory.get_path() + ':')
    directory.display()
    print()
    if directory.recursive:
        for i in range(len(directories)):
            display_dir(directories[i], display_name_dir)


def manage_display(files, directories):
    display_name_dir = False

    for f in files:
        f.display()

    if len(files) > 0 and len(directories) > 0:
        print()

    if len(files) > 0 or len(directories) > 1:
        display_name_dir = True

    for d in directories:
        display_dir(d, display_name_dir)


def manage_files(files, options_dic):
    file_list = []

    for f in files:
        file = File(f, f)
        for key, value in options_dic.items():
            if value:
                OPTION_MAP[key](file)
        file_list.append(file)

    return file_list


def resolve_dir(directory, options_dic):
    get_dirs_and_files(directory)
    for key, value in options_dic.items():
        if value:
            OPTION_MAP[key](directory)
    if directory.recursive:
        for d in directory.get_directories():
            resolve_dir(d, options_dic)


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
    manage_display(files, directories)


OPTION_MAP = {
    'all': all_option,
    'long': long_option,
    'count': count_option,
    'directory': directory_option,
}
