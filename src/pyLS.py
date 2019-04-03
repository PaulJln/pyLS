import argparse


def all_option():
    print("this is all")


def recursive_option():
    print("this is recursive")


OPTION_MAP = {
    'all': all_option,
    'Recursive': recursive_option
}


def manage_options():
    parser = argparse.ArgumentParser(prog='pyLS.py')
    parser.add_argument('-a', '--all', action='store_true', help='Display additional hidden files or directories')
    parser.add_argument('-R', '--Recursive', action='store_true', help='Recursive display')
    parser.add_argument('-l', action='store_true', help='Display the size of files or directories')
    parser.add_argument('-c', action='store_true', help='Display number of lines in the file')
    parser.add_argument('-d', '--directory', action='store_true',
                        help='Display only directories, and the number of file in each')
    parser.add_argument('-r', '--reverse', action='store_true', help='Reverse the display order')
    args = parser.parse_args()

    d = vars(args)

    for key, value in d.items():
        if value:
            OPTION_MAP[key]()
    print(d)


def main():
    manage_options()


main()
