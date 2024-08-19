# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
#name = input("HeLo WAT Name you")
#b_size = int(input(f"{name}, please choose b size"))
#print(f"{name}, the board size is: {b_size}, number of mines is: anfkja")

name = input('Hello, whats your name')

if len(name) <= 2:
    name = None
    board_size = None
    number_of_mines = None
    print("Your name is too short")
else:
    board_size = int(input(f"{name}, please choose board size"))
    if board_size > 0 and board_size < 26:
        number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
        grid_size = board_size**2
        half_grid_size = grid_size/2
        if number_of_mines > 0 and number_of_mines <= half_grid_size:
            number_of_mines = number_of_mines
        else:
            print(f"{name}, you have entered illegal number of mines")
    else:
        board_size = None
        number_of_mines = None
        print(f"{name}, you have entered illegal board size")


