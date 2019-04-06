from .classes.Directory import Directory
from .classes.File import File
from .classes.ExplorerHelper import ExplorerHelper


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


OPTION_MAP = {
    'all': all_option,
    'long': long_option,
    'count': count_option,
    'directory': directory_option,
}
