class Information:
    def __init__(self, name, size=0):
        self._name = name
        self._size = size
        self._display = []

    def get_name(self):
        return self._name

    def get_display(self):
        return self._display

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size


class Directory(Information):
    def __init__(self, name, recursive, reverse):
        super().__init__(name)
        self.recursive = recursive
        self.reverse = reverse
        self.__directories = []
        self.__files = []

    def get_nb_files(self):
        return len(self.__files)

    def get_directories(self):
        return self.__directories

    def get_files(self):
        return self.__files

    def add_directory(self, directory):
        self.__directories.append(directory)
        self._display.append(directory.get_name())

    def add_file(self, file):
        self.__files.append(file)
        self._display.append(file.get_name())

    def clear_files(self):
        self.__files.clear()

    def display(self):
        display = self.__directories + self.__files
        display.sort(key=lambda inst: inst.get_name(), reverse=self.reverse)
        for d in display:
            print(d.get_name())


class File(Information):
    def __init__(self, name, size=0, nb_lines=0):
        super().__init__(name, size)
        self.__nb_lines = nb_lines

    def get_nb_lines(self):
        return self.__nb_lines

    def set_nb_lines(self, nb_lines):
        self.__nb_lines = nb_lines
