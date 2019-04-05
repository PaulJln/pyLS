from .utils import Directory
from .ExplorerHelper import ExplorerHelper


def get_dirs_and_files(root):
    ExplorerHelper.basic_search(root)


def all_option(root):
    ExplorerHelper.hidden_search(root)


def long_option(root):
    ExplorerHelper.get_size(root)


def count_option(root):
    ExplorerHelper.get_files_nb_lines(root)


def directory_option(root):
    root.get_files().clear()
    ExplorerHelper.get_nb_files(root)


def display(root):
    root.display()


def manage_options(options_dic, paths, recursive, reverse):
    if not paths:
        paths = '.'
    for path in paths:
        root = Directory(path, recursive, reverse)
        get_dirs_and_files(root)
        for key, value in options_dic.items():
            if value:
                OPTION_MAP[key](root)
        display(root)


OPTION_MAP = {
    'all': all_option,
    'long': long_option,
    'count': count_option,
    'directory': directory_option,
}
