# This is how to use function in the todo app

import functions


# print(help(get_todos))
# print(help(write_todos))

def parse_input(user_input_, slicing_index):
    return user_input_[slicing_index:]

def structure_todos(todos_local):

    for i, item in enumerate(todos_local):
        item = item.strip("\n")
        todos_list = f"{i + 1}-{item}"
        print(todos_list)



while True :
    try:
        user_input = input("Type add, show, edit, complete or exit: ")

        user_input = user_input.lower().strip()


        if user_input.startswith("add"):
            # first we read file
            parsed_input = parse_input(user_input, 4)

            if parsed_input== "" :
                todo = input("Enter your todo: ")
            else:
               todo = parsed_input


            existing_todos = functions.get_todos("todos.txt")


            existing_todos.append(todo+ "\n")

            # we can write the parameter variable on function call to make it clear,
            # which argument is passed into which variable
            functions.write_todos(existing_todos)
            message = f"New todo `{todo}` has been added"
            print(message)


        elif user_input.startswith("show") :

            todos = functions.get_todos()
            # method -1
            # new_todo = []
            #
            # for item in todos:
            #     new_todo.append(item.strip("\n"))


            # method -2 (list comprehension)

            # new_todos = [item.strip("\n") for item in todos]
            # print(new_todos)

            # method 3- simple solution
            structure_todos(todos)



        elif user_input.startswith("edit"):

            todos = functions.get_todos("todos.txt")

            parsed_input = parse_input(user_input, 5)

            if parsed_input == "":
                structure_todos(todos)
                todo_number = int(input("Which todo you want to edit?: "))
            else:
                todo_number = int(parsed_input)


            if todo_number > len(todos):
                print("You have entered the wrong todo number")
                continue

            todo_index = todo_number - 1
            new_todo = input ("Enter new todo: ")
            todos[todo_index] = new_todo + "\n"


            functions.write_todos(todos)

            print("Todo has been edited")

        elif user_input.startswith("complete") :

            todos = functions.get_todos()

            parsed_input = parse_input(user_input,9 )

            if parsed_input =="":
                structure_todos(todos)
                completed_todo_number = int(input("Which todo you want to mark as completed?: "))
            else:
                completed_todo_number = int(parsed_input)


            if completed_todo_number > len(todos):
                print("You have entered the wrong todo number")
                continue

            todo_index = completed_todo_number - 1

            completed_todo = todos.pop(todo_index).strip("\n")

            functions.write_todos(todos)

            print(f"'{completed_todo}' marked as completed and removed from the list")

        elif user_input.startswith("exit") :
            break

        else:
            print("Invalid command")

    except ValueError:
        print("Please enter a valid number")