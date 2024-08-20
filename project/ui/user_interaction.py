# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
#name = input("HeLo WAT Name you")
#b_size = int(input(f"{name}, please choose b size"))
#print(f"{name}, the board size is: {b_size}, number of mines is: anfkja")
def is_name_valid(name):
    if len(name) > 2:
        return True , name
    else:
        return False

def is_board_size_valid(board_size):
    if board_size > 0 and board_size < 26 and board_size != None:
        return True
    else:
        return False


def is_number_of_mines_valid(board_size, number_of_mines):
    grid_size = board_size ** 2
    half_grid_size = grid_size / 2
    if number_of_mines > 0 and number_of_mines <= half_grid_size and number_of_mines != None:
        return True
    else:
        return False


def register_user():
    name = input('Hello, whats your name')
    board_size = None
    number_of_mines = None
    if is_name_valid(name):
        board_size = int(input(f"{name}, please choose board size"))
        if is_board_size_valid(board_size):
            number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
            if not is_number_of_mines_valid(board_size, number_of_mines):
                number_of_mines = None
                print(f"{name}, you have entered illegal number of mines")

            else:
                return name, board_size, number_of_mines
        else:
            board_size = None
            print(f"{name}, you have entered illegal board size")
            return name, board_size, number_of_mines
    else:
        print("Your name is too short")
        name = None
        return name, board_size, number_of_mines







user_name, user_board_size, user_num_mines = register_user()
print(f"name:{user_name}, board size:{user_board_size}, number of mines:{user_num_mines}")
