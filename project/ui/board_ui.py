from bokeh.colors.named import linen

import project.board.board_functions as bc


def parse_cmd(command):
    command_name = command.split(" ")[0]
    parameters = command.split(" ")[1:len(command)]
    return command_name, parameters

def draw_board(board):
    first_line = []
    lines = []
    matrix = ""
    for i in range(len(board)):
        if i == 0:
            first_line.append(" ")
        first_line.append(chr(65 + i))
    lines.append(first_line)
    for i in range(len(board)):
        line = [str(i)]
        for k in board[i]:
            line.append(str(k))
        lines.append(line)
    for i in lines:
        if lines[0] == i:
            s = "   ".join(i) + '\n'
        else:
            s = " | ".join(i) + '\n'
        matrix += s
    return matrix

print(draw_board(board))

def convert_coords(location):
    row_number = ""
    col_number  = ""
    for i in location:
        if (i.isdigit()):
            row_number += i
        else:
            col_number  += i
    row_number = int(row_number)
    col_number = ord(col_number) - ord('A')
    return row_number, col_number

