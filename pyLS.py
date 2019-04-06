import argparse
from src.pyLS_pkg import managers


def manage_args():
    parser = argparse.ArgumentParser(prog='pyLS.py')

    parser.add_argument('-a', '--all', action='store_true', help='Display additional hidden files or directories')
    parser.add_argument('-R', '--Recursive', action='store_true', help='Recursive display')
    parser.add_argument('-l', '--long', action='store_true', help='Display the size of files or directories')
    parser.add_argument('-c', '--count', action='store_true', help='Display number of lines in the file')
    parser.add_argument('-d', '--directory', action='store_true',
                        help='Display only directories, and the number of file in each')
    parser.add_argument('-r', '--reverse', action='store_true', help='Reverse the display order')
    parser.add_argument('paths', action='store', nargs='*', help="Directory path, can be a list of path")

    args = parser.parse_args()
    args_dic = vars(args)

    reverse = args.reverse
    recursive = args.Recursive
    paths = args.paths

    delattr(args, "reverse")
    delattr(args, "Recursive")
    delattr(args, "paths")

    return_value = managers.manage_options(args_dic, paths, recursive, reverse)
    exit(return_value)


def main():
    manage_args()


main()
