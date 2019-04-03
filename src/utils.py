class Information:
    def __init__(self, name='', size=0):
        self._name = name
        self._size = size

    def get_name(self):
        return self._name

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size


class Directory(Information):
    def __init__(self, name=''):
        super().__init__(name)
        self.__nbFiles = 0

    def get_nb_files(self):
        return self.__nbFiles

    def set_nb_files(self, nb_files):
        self.__nbFiles = nb_files


class File(Information):
    def __init__(self, name='', size=0, nb_lines=0):
        super().__init__(name, size)
        self.__nb_lines = nb_lines

    def get_nb_lines(self):
        return self.__nb_lines

    def set_nb_lines(self, nb_lines):
        self.__nb_lines = nb_lines
