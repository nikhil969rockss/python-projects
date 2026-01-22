def get_todos(filename="todos.txt", filemode="r"):
    """ Returns a list of todos
    (filename="todo.txt", filemode="r") default
    you can change the filename and filemode
    """
    with open(filename, filemode) as file_local:
        local_todos = file_local.readlines()

    return local_todos



def write_todos(todos_list, filepath="todos.txt"):
    """ Write todos in a file
        (todos_list=list,filename="todo.txt") default
        you can change the filename
        """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_list)
