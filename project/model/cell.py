# This is a start of a Cell, this code is WRONG
# Fix it and add all the required capabilities
from IPython.core.magic import cell_magic
from sympy.codegen.ast import continue_
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

    def set_flag(self):
        self.flag = True

    def is_flaged(self):
        return self.flag

    def str_as_hidden(self):
        if not self.is_clicked() and not self.is_flaged():
            self.flag = '_'
            return self.flag
        elif self.is_flaged():
            self.flag = 'F'
            return self.flag

    def str_as_clicked(self):
        try:
            if self.is_clicked():
                return str(self.clicked)
        except NotImplementedError as e:
            return f"Invalid input: {str(e)}"

    def __str__(self):
        if self.is_clicked():
            return self.str_as_clicked()
        else:
            return self.str_as_hidden()



