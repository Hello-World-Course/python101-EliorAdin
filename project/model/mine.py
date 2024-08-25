from project.model.cell import Cell


class Mine(Cell):

    def __init__(self, x, y):
        super().__init__(x,y)
        self.x = x
        self.y = y


    def str_as_clicked(self):
        if self.clicked:
            self.clicked = '*'
            return str(self.clicked)
        else:
            self.clicked = ' '
            return str(self.clicked)

mine = Mine(x=3 ,y=3)
print(mine)

