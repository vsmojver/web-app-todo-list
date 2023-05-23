def get_todos(filepath="todos.txt"):
    """ Read a text file and return list
    of to-do items
    """
    with  open(filepath, 'r') as file_local:
        todos=file_local.readlines()
    return todos

def write_todos(todos_arg, filepath="todos.txt"):
    """ Writhe the to-do items list in the text file."""
    with  open(filepath, 'w') as file:      
        file.writelines(todos_arg)
    