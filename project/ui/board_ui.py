def parse_cmd(command):
    command_name = command.split(" ")[0]
    parameters = command.split(" ")[1:len(command)]
    return command_name, parameters

board = [["_",2,"_"], ["_",1,"_"], ["_",0,"_"]]

def draw_board(board):
    fist_line = []
    for i in range(len(board)):
        fist_line.append(chr(65 + i))
        s = "   ".join(fist_line)
    print("    " +s)
    for i in range(len(board)):
        line = [str(i)]
        for k in board[i]:
            line.append(str(k))
            s = " | ".join(line)
        print (s)

def convert_coords(location):
    pass
draw_board(board)