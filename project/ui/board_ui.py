def parse_cmd(command):
    # This is wrong but close, you should fix it
    command_name = command.split(" ")[0]
    parameters = command.split(" ")[1:len(command)]
    return command_name, parameters
