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
