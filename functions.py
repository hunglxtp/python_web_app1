FILEPATH = "files/todos.text"


def get_todos(filepath=FILEPATH) -> list:
    """ Read the todo file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write todos items list
    to file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
