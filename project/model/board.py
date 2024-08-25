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
        self.inner_board[x][y] = Cell(x,y)
        self.inner_board[x][y].is_flaged()

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
print(board.inner_board)
print(board[2][2].set_flag(0, 0))
