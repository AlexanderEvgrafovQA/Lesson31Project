class Transport:
    def __init__(self, width, lenght, number):
        self._width = width
        self._lenght = lenght
        self._number = number

    @property
    def square(self):
        return self._width * self._lenght

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise Exception()

    @width.deleter
    def width(self):
        del self._width

    @property
    def lenght(self):
        return self._lenght

    @lenght.setter
    def lenght(self, lenght):
        if lenght > 0:
            self._lenght = lenght
        else:
            raise Exception()

    @lenght.deleter
    def lenght(self):
        del self._lenght

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @lenght.deleter
    def number(self):
        del self._number

    def __str__(self):
        return (f"width = {self._width}, "
                f"width = {self._lenght}, "
                f"width = {self._number}")
