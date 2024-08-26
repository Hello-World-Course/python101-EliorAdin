from project.model.empty_cell import EmptyCell
from project.model.mine import Mine

class Board():
    def __init__(self ,board_size):
        self.board_size = board_size
        self.inner_board = []

        for i in range(board_size):
            line = []
            for j in range(board_size):
                cell = EmptyCell(x=i, y=j)
                line.append(cell)
            self.inner_board.append(line)

    def __len__(self):
        return len(self.inner_board)

    def __getitem__(self, key):
        return self.inner_board[key]


    def set_flag(self,x ,y):
        self.inner_board[x][y].__str__()

    def reveal_all(self):
        for i in range(len(self.inner_board)):
            for j in range(len(self.inner_board[i])):
                if not self.inner_board[i][j].is_clicked():
                    self.inner_board[i][j].set_clicked()
                    return self.inner_board[i][j].str_as_clicked()


def draw_board(board):
    first_line = []
    lines = []
    matrix = ""
    for i in range(len(board)):
        if i == 0:
            first_line.append("  ")
        first_line.append(chr(65 + i))
    lines.append(first_line)
    for i in range(len(board.inner_board)):
        line = [str(i) + " "]
        for j in range(len(board.inner_board[i])):
            if not board[i][j].is_clicked():
                line.append(board[i][j].str_as_hidden())
            else:
                line.append(board[i][j].str_as_clicked())
        lines.append(line)
    for i in lines:
        if lines[0] == i:
            s = " ".join(i) + ' \n'
        else:
            s = "|".join(i) + '|\n'
        matrix += s
    return matrix
board = Board(3)
# will print True
print(isinstance(board[0][0], EmptyCell))

# will print 3
print(len(board))


board[1][2] = Mine(x=1, y=2)
board[0][2] = Mine(x=0, y=2)
board[0][1].set_value(1)
board[1][1].set_value(2)
board[2][1].set_value(1)
board[2][2].set_value(1)
board[2][2].set_flag()


board.reveal_all()
print(draw_board(board))