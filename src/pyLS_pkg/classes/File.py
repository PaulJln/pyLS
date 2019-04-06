from .Information import Information


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