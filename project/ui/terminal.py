#from matplotlib.pyplot import get_current_fig_manager
#from sympy.physics.units import current
import project.ui.user_interaction as ui
from project.model.board import Board
import board_ui as b_ui
from project.model.mine import Mine

class Terminal:

    def __init__(self):
        self.name = None
        self.current_board = None
        self.number_of_mines = None
        self.board_size = None

    def init_game(self):
            self.name, self.board_size, self.number_of_mines = ui.register_user()
            if self.name is not None or self.number_of_mines is not None or self.board_size is not None:
                self.current_board = Board(self.board_size)



    def create_string_(self):
        if self.name is not None or self.number_of_mines is not None or self.board_size is not None:
            return b_ui.draw_board(self.current_board)
        else:
            return "Failed to init game"

    def draw(self):
        print(self.create_string_())


terminal = Terminal()
terminal.init_game()

terminal.draw()
terminal.current_board[0][0] = Mine(x=0, y=0)
terminal.current_board[0][1].set_value(1)
terminal.current_board[1][0].set_value(1)
terminal.current_board[1][1].set_value(1)
terminal.current_board.reveal_all()


terminal.draw()

