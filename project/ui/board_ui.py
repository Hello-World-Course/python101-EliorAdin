def parse_cmd(command):
    # This is wrong but close, you should fix it
    command_name = command.split(" ")[0]
    parameters = command.split(" ")[1]
    return command_name, parameters


# This is a run example, use this to verify your code
# you should remove this code later
command, parameters = parse_cmd("test_command a b c d e")
print(f"This is the command: {command}")
print(f"This is the parameters: {parameters}")