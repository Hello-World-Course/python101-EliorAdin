#from matplotlib.pyplot import get_current_fig_manager
#from sympy.physics.units import current

import project.ui.user_interaction as ui
from project.model.board import Board
import board_ui as b_ui
from project.model.mine import Mine
from project.model.empty_cell import EmptyCell

class Terminal():

    def __init__(self):
        self.name = None
        self.current_board = None
        self.number_of_mines = None
        self.board_size = None

    def init_game(self):
            self.name, self.board_size, self.number_of_mines = ui.register_user()
            if  self.name is None or self.number_of_mines is None or self.board_size is None:
                return "Failed to init game"
            else:
                self.current_board = Board(self.board_size)



    def create_string_(self):
        return b_ui.draw_board(self.current_board)

    def draw(self):
        print(self.create_string_())

