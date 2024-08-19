# THIS CODE IS WRONG, FIX IT AND ADD NEW CODE
#name = input("HeLo WAT Name you")
#b_size = int(input(f"{name}, please choose b size"))
#print(f"{name}, the board size is: {b_size}, number of mines is: anfkja")

name = input('Hello, whats your name')

if len(name) <= 2:
    name = None
    exit("Your name is too short")
else:
    board_size = int(input(f"{name}, please choose board size"))

if board_size > 0 and board_size < 26:
    number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
else:
    board_size = None
    exit(f"{name}, you have entered illegal board size")

if number_of_mines == 0 and not number_of_mines <= board_size/2:
    number_of_mines = None
    exit(f"{name}, you have entered illegal number of mines")
