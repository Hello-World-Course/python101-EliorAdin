from project.model.cell import Cell

class EmptyCell(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.value = " "

    def set_value(self, value):
        if 0 < value <= 8:
            self.value = value




    def get_value(self):
        return self.value

    def str_as_clicked(self):
        if self.is_clicked():
            return str(self.get_value())



