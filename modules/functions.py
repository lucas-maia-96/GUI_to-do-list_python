FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file: 
        todos_f = file.readlines()
    return todos_f

def write_todos(todos_f, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_f)