def all_option(path):
    print("this is all")


def recursive_option(path):
    print("this is recursive")


def long_option(path):
    print("this is long")


def count_option(path):
    print("this is count")


def directory_option(path):
    for value in path:
        print("this is directory " + value)


def reverse_option(path):
    print("this is reverse")


def manage_display(args_dic, path):
    display = []
    for key, value in args_dic.items():
        if key != 'path' and value:
            OPTION_MAP[key](display, path)


OPTION_MAP = {
    'all': all_option,
    'Recursive': recursive_option,
    'long': long_option,
    'count': count_option,
    'directory': directory_option,
    'reverse': reverse_option
}
