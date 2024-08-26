from project.model.cell import Cell


class Mine(Cell):

    def __init__(self, x, y):
        super().__init__(x,y)
        self.x = x
        self.y = y


    def str_as_clicked(self):
        if self.is_clicked():
            self.clicked = '*'
            return self.clicked
        else:
            self.clicked = '_'
            return self.clicked




