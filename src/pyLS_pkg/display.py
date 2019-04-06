import sys
CURSOR_UP_ONE = '\x1b[1A'


def display_dir(directory, display_name_dir):
    directories = directory.get_directories()
    directories.sort(key=lambda inst: inst.get_name().strip('.'))
    if directory.get_path() and display_name_dir or directory.recursive:
        print(directory.get_path() + ':')
    directory.display()
    if directory.recursive:
        for i in range(len(directories)):
            display_dir(directories[i], display_name_dir)


def display(files, directories):
    display_name_dir = False

    for f in files:
        f.display()

    if directories:
        if len(files) > 0:
            print()

        if len(files) > 0 or len(directories) > 1:
            display_name_dir = True

        for d in directories:
            display_dir(d, display_name_dir)
        sys.stdout.write(CURSOR_UP_ONE)