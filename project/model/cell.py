# This is a start of a Cell, this code is WRONG
# Fix it and add all the required capabilities
from twisted.words.xish.domish import elementStream


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.clicked = False
        self.flag = False


    def is_clicked(self):
        return self.clicked

    def set_clicked(self):
        self.clicked = True

    def set_flag(self ,x ,y):
        self.flag = True
        self.x = x
        self.y = y

    def is_flaged(self):
        return self.flag

    def str_as_hidden(self):
        if not self.is_clicked() and not self.is_flaged():
            self.flag = '_'
        elif self.is_flaged():
            self.flag = 'F'

    def str_as_clicked(self):
        try:
            pass
        except NotImplementedError as e:
             return f"Invalid input: {str(e)}"

    def __str__(self):
        if not self.is_clicked:
            return str(self.str_as_hidden())
        else:
            return str(self.str_as_clicked())
