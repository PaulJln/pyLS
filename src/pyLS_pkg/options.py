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


def manage_display(files, directories):
    display_name_dir = False

    for f in files:
        f.display()

    if len(files) > 0 and len(directories) > 0:
        print()

    if len(files) > 0 or len(directories) > 1:
        display_name_dir = True

    for i in range(len(directories)):
        if display_name_dir or directories[i].recursive:
            print(directories[i].get_path() + ':')
        directories[i].display()
        if i < len(directories) - 1:
            print()


def manage_files(files, options_dic):
    file_list = []

    for f in files:
        file = File(f, f)
        for key, value in options_dic.items():
            if value:
                OPTION_MAP[key](file)
        file_list.append(file)

    return file_list


def manage_directories(directories, options_dic, recursive, reverse):
    dir_list = []

    for d in directories:
        directory = Directory('', d, recursive, reverse)
        get_dirs_and_files(directory)
        for key, value in options_dic.items():
            if value:
                OPTION_MAP[key](directory)
        dir_list.append(directory)

    return dir_list


def manage_options(options_dic, paths, recursive, reverse):
    if not paths:
        paths.append('.')
    paths = split_dirs_files(paths)
    if reverse:
        paths["files"].reverse()
        paths["dirs"].reverse()
    print(paths)
    files = manage_files(paths["files"], options_dic)
    directories = manage_directories(paths["dirs"], options_dic, recursive, reverse);
    manage_display(files, directories)


OPTION_MAP = {
    'all': all_option,
    'long': long_option,
    'count': count_option,
    'directory': directory_option,
}
