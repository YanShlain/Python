def command_one():
    print("Command ONE invoked")


def command_two():
    print("Command TWO invoked")


def command_three():
    print("Command THREE invoked")


commands = [command_one, command_two, command_three]

for cmd in commands:
    cmd()

