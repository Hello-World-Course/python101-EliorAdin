def is_on_board(x, y, board):
    # This is wrong fix it:
    if len(board) > x > -1:
        if len(board[x]) > y > -1:
            return True
        else:
            return False
    else:
        return False

def safe_set_value(x, y, value, board):
    if len(board) > x > -1:
        if len(board[x]) > y > -1:
            board[x][y] = value
            return True
        else:
            return False
    else:
        return False

def create_empty_board(board_size, initial_value):
    board = []
    for i in range(board_size):
        board.append([])
        for _ in range(board_size):
            board[i].append(initial_value)
    print(board)
    return board



