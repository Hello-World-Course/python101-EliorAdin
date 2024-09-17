from project.model.cell import Cell


class Mine(Cell):


    def str_as_clicked(self):
        if self.is_clicked():
            self.clicked = '*'
            return self.clicked
        else:
            self.clicked = '_'
            return self.clicked
