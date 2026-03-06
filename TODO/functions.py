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


def remove_new_lines(todos_list):
    """Removes \n from the todos list"""
    return [todo.replace("\n", "") for todo in todos_list]


def add_new_line(todos_list):
    """Adds a '\n at the end of the todos"""
    todos = []
    for todo in todos_list:
        if  "\n" in todo:
              todos.append(todo)
        else:
            todos.append(todo+"\n")
    return todos

print(__name__)
if __name__ == "__main__":
    print(add_new_line(["learn python\n", "new todo"]))