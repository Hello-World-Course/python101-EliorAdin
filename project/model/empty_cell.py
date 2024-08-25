from project.model.cell import Cell

class EmptyCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.value = "_"

    def set_value(self, value):
        if 0 < value <= 8:
            self.value = value
        elif 0 == value:
            self.value = " "

    def get_value(self):
        return self.value

    def str_as_clicked(self):
        if self.value:
            val = self.get_value()
            return str(val)
        else:
            pass


