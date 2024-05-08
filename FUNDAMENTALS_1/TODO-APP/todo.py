exit = False

todo_items = []

def get_argument(command):
    try:
        command_name, argument = command.split(" ", maxsplit=1)
        return argument
    except ValueError:
        return ""  # Return empty string if there's no argument

def handle_add_command(command):
    argument = get_argument(command)
    if argument:
        print("Adding task:", argument)
        todo_items.append(argument)
    else:
        print("No task specified")

def handle_delete_command(command):
    argument = get_argument(command)
    if argument:
        try:
            print("Deleting task:", argument)
            todo_items.remove(argument)
        except ValueError:
            print("Task not found")
    else:
        print("No task specified to delete")

def handle_list_command():
    print("Todo items:")
    for index, item in enumerate(todo_items):
        print(f"{index + 1}. {item}")

def handle_save_command(command):
    filename = get_argument(command)
    if filename:
        filename += ".todo.txt"
        try:
            with open(filename, 'w') as file:
                for item in todo_items:
                    file.write(f"{item}\n")
            print(f"Saved to {filename}")
        except IOError as e:
            print(f"Could not save file: {e}")
    else:
        print("No filename specified")

def handle_open_command(command):
    filename = get_argument(command)
    if filename:
        filename += ".todo.txt"
        try:
            with open(filename, 'r') as file:
                todo_items.clear()
                for line in file:
                    todo_items.append(line.strip())
            print(f"Loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found")
        except IOError as e:
            print(f"Could not open file: {e}")
    else:
        print("No filename specified to open")

def process_command(command):
    global exit

    if command == "exit":
        exit = True
    elif command.startswith("add"):
        handle_add_command(command)
    elif command.startswith("delete"):
        handle_delete_command(command)
    elif command == "list":
        handle_list_command()
    elif command.startswith("open"):
        handle_open_command(command)
    elif command.startswith("save"):
        handle_save_command(command)
    else:
        print("Command not recognized")
    
    return exit


while not exit:
    command = input("Enter command: ")
    exit = process_command(command)