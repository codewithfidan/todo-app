FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items."""
    with open(filepath, "r") as file_locaL:
        todos_local = file_locaL.readlines()  # returns a list
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)
