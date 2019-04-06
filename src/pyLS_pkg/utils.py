class Information:
    def __init__(self, name, path):
        self._name = name
        self._size = 0
        self._display = []
        self._display.append(name)
        self._path = path

    def get_name(self):
        return self._name

    def get_path(self):
        return self._path

    def get_display(self):
        return self._display

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._display.append(size)
        self._size = size


class Directory(Information):
    def __init__(self, name, path, recursive, reverse):
        super().__init__(name, path)
        self.__nb_files = 0
        self.recursive = recursive
        self.reverse = reverse
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
        display = self.__directories + self.__files
        display.sort(key=lambda inst: inst.get_name(), reverse=self.reverse)
        for d in display:
            print(*d.get_display(), sep=' ')


class File(Information):
    def __init__(self, name, path):
        super().__init__(name, path)
        self.__nb_lines = 0

    def get_nb_lines(self):
        return self.__nb_lines

    def set_nb_lines(self, nb_lines):
        self._display.append(nb_lines)
        self.__nb_lines = nb_lines

    def display(self):
        print(*self.get_display(), sep=' ')
