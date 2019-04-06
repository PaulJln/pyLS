from .Information import Information


class Directory(Information):
    def __init__(self, name, path, recursive, reverse):
        super().__init__(name, path)
        self.recursive = recursive
        self.reverse = reverse
        self.__nb_files = 0
        self.__directories = []
        self.__files = []

    def __repr__(self):
        return self._name

    def set_nb_files(self, nb_files):
        self._display.append(nb_files)
        self.__nb_files = nb_files

    def get_directories(self):
        return self.__directories

    def get_files(self):
        return self.__files

    def add_directory(self, directory):
        self.__directories.append(directory)

    def add_file(self, file):
        self.__files.append(file)

    def clear_files(self):
        self.__files.clear()

    def display(self):
        if self._path:
            display = self.__directories + self.__files
            display.sort(key=lambda inst: inst.get_name().strip('.'), reverse=self.reverse)
            for d in display:
                print(*d.get_display(), sep=' ')
            print()