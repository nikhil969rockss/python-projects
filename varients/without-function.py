# This is program for having the consistent data on text file



#
# while True :
#     user_input = input("Type add, show, edit, complete or exit: ")
#
#     user_input = user_input.lower().strip()
#
#     match user_input :
#         case 'add' :
#             # first we read file
#             todo = input("Enter your todo: ") + "\n"
#
#             file = open("todos.txt", "r")
#             existing_todos = file.readlines()
#             file.close()
#
#             existing_todos.append(todo)
#
#             file = open("todos.txt", "w")
#             file.writelines(existing_todos)
#             file.close()
#
#         case 'show' :
#             file = open("todos.txt", "r")
#             todos = file.readlines()
#             file.close()
#             for index, todo in enumerate(todos) :
#                 print(f"{index+1}-{todo}")
#
#         case 'edit':
#             for index, todo in enumerate(todos):
#                 print(f"{index + 1}-{todo}")
#
#             todo_number = int(input("Enter todo number you want to edit: "))
#             if todo_number > len(todos):
#                 print("You have entered the wrong todo number")
#                 continue
#
#             todo_index = todo_number - 1
#             new_todo = input ("Enter new todo: ")
#             todos[todo_index] = new_todo
#             print("Todo has been edited")
#
#         case 'complete':
#             for index, todo in enumerate(todos):
#                 print(f"{index + 1}-{todo}")
#
#             completed_todo_number = int(input("Enter todo number you want to complete: "))
#             if completed_todo_number > len(todos):
#                 print("You have entered the wrong todo number")
#                 continue
#
#             todos.pop(completed_todo_number -1)
#             print("Todo marked as completed")
#         case 'exit' :
#             break




# This is the 'show todo' case of the above example


#
# while True :
#     user_input = input("Type add, show, edit, complete or exit: ")
#
#     user_input = user_input.lower().strip()
#
#     match user_input :
#         case 'add' :
#             # first we read file
#             todo = input("Enter your todo: ")
#
#             file = open("todos.txt", "r")
#             existing_todos = file.readlines()
#             file.close()
#
#             existing_todos.append(todo+ "\n")
#
#             file = open("todos.txt", "w")
#             file.writelines(existing_todos)
#             file.close()
#
#         case 'show' :
#             file = open("todos.txt", "r")
#             todos = file.readlines()
#             file.close()
#
#             # method -1
#             # new_todo = []
#             #
#             # for item in todos:
#             #     new_todo.append(item.strip("\n"))
#
#
#             # method -2 (list comprehension)
#
#             # new_todos = [item.strip("\n") for item in todos]
#             # print(new_todos)
#
#             # method 3- simple solution
#
#
#             for index, todo in enumerate(todos) :
#                 todo = todo.strip("\n")
#                 print(f"{index+1}-{todo}")
#
#         case 'edit':
#             for index, todo in enumerate(todos):
#                 print(f"{index + 1}-{todo}")
#
#             todo_number = int(input("Enter todo number you want to edit: "))
#             if todo_number > len(todos):
#                 print("You have entered the wrong todo number")
#                 continue
#
#             todo_index = todo_number - 1
#             new_todo = input ("Enter new todo: ")
#             todos[todo_index] = new_todo
#             print("Todo has been edited")
#
#         case 'complete':
#             for index, todo in enumerate(todos):
#                 print(f"{index + 1}-{todo}")
#
#             completed_todo_number = int(input("Enter todo number you want to complete: "))
#             if completed_todo_number > len(todos):
#                 print("You have entered the wrong todo number")
#                 continue
#
#             todos.pop(completed_todo_number -1)
#             print("Todo marked as completed")
#         case 'exit' :
#             break



# completing the 'edit' and 'complete' case

# while True :
#     user_input = input("Type add, show, edit, complete or exit: ")
#
#     user_input = user_input.lower().strip()
#
#     match user_input :
#         case "add" :
#             # first we read file
#             todo = input("Enter your todo: ")
#
#
#             # using with context manger
#
#             with open("todos.txt", "r") as file :
#                 existing_todos = file.readlines()
#
#
#             existing_todos.append(todo+ "\n")
#
#             with open("todos.txt", "w") as file :
#                 file.writelines(existing_todos)
#
#
#         case 'show' :
#
#             with open("todos.txt", "r") as file :
#                 todos = file.readlines()
#
#             # method -1
#             # new_todo = []
#             #
#             # for item in todos:
#             #     new_todo.append(item.strip("\n"))
#
#
#             # method -2 (list comprehension)
#
#             # new_todos = [item.strip("\n") for item in todos]
#             # print(new_todos)
#
#             # method 3- simple solution
#
#
#             for index, todo in enumerate(todos) :
#                 todo = todo.strip("\n")
#                 print(f"{index+1}-{todo}")
#
#         case 'edit':
#
#             with open("todos.txt", "r") as file :
#                 todos = file.readlines()
#
#             for index, todo in enumerate(todos):
#                 todo = todo.strip("\n")
#                 print(f"{index + 1}-{todo}")
#
#             todo_number = int(input("Which todo you want to edit?: "))
#             if todo_number > len(todos):
#                 print("You have entered the wrong todo number")
#                 continue
#
#             todo_index = todo_number - 1
#             new_todo = input ("Enter new todo: ")
#             todos[todo_index] = new_todo + "\n"
#
#             with open("todos.txt", "w") as file :
#                 file.writelines(todos)
#
#             print("Todo has been edited")
#
#         case 'complete':
#             with open("todos.txt", "r") as file:
#                 todos = file.readlines()
#
#             for index, todo in enumerate(todos):
#                 todo = todo.strip("\n")
#                 print(f"{index + 1}-{todo}")
#
#             completed_todo_number = int(input("Which todo you want to mark as completed?: "))
#             if completed_todo_number > len(todos):
#                 print("You have entered the wrong todo number")
#                 continue
#
#             todo_index = completed_todo_number - 1
#
#             completed_todo = todos.pop(todo_index).strip("\n")
#
#             with open("todos.txt", "w") as file:
#                 file.writelines(todos)
#
#             print(f"'#{completed_todo}' marked as completed and removed from the list")
#
#         case 'exit' :
#             break



#  creating the program with if/else

# while True :
#     user_input = input("Type add, show, edit, complete or exit: ")
#
#     user_input = user_input.lower().strip()
#
#
#     if 'add' in user_input:
#         # first we read file
#         if user_input[4:]== "" :
#             todo = input("Enter your todo: ")
#         else:
#            todo = user_input[4:]
#
#
#         # using with context manger
#
#         with open("todos.txt", "r") as file :
#             existing_todos = file.readlines()
#
#
#         existing_todos.append(todo+ "\n")
#
#         with open("todos.txt", "w") as file :
#             file.writelines(existing_todos)
#
#
#     elif 'show' in user_input :
#
#         with open("todos.txt", "r") as file :
#             todos = file.readlines()
#
#         # method -1
#         # new_todo = []
#         #
#         # for item in todos:
#         #     new_todo.append(item.strip("\n"))
#
#
#         # method -2 (list comprehension)
#
#         # new_todos = [item.strip("\n") for item in todos]
#         # print(new_todos)
#
#         # method 3- simple solution
#
#
#         for index, todo in enumerate(todos) :
#             todo = todo.strip("\n")
#             print(f"{index+1}-{todo}")
#
#     elif 'edit' in user_input:
#
#         with open("todos.txt", "r") as file :
#             todos = file.readlines()
#
#         for index, todo in enumerate(todos):
#             todo = todo.strip("\n")
#             print(f"{index + 1}-{todo}")
#
#         todo_number = int(input("Which todo you want to edit?: "))
#         if todo_number > len(todos):
#             print("You have entered the wrong todo number")
#             continue
#
#         todo_index = todo_number - 1
#         new_todo = input ("Enter new todo: ")
#         todos[todo_index] = new_todo + "\n"
#
#         with open("todos.txt", "w") as file :
#             file.writelines(todos)
#
#         print("Todo has been edited")
#
#     elif 'complete' in user_input:
#         with open("todos.txt", "r") as file:
#             todos = file.readlines()
#
#         for index, todo in enumerate(todos):
#             todo = todo.strip("\n")
#             print(f"{index + 1}-{todo}")
#
#         completed_todo_number = int(input("Which todo you want to mark as completed?: "))
#         if completed_todo_number > len(todos):
#             print("You have entered the wrong todo number")
#             continue
#
#         todo_index = completed_todo_number - 1
#
#         completed_todo = todos.pop(todo_index).strip("\n")
#
#         with open("todos.txt", "w") as file:
#             file.writelines(todos)
#
#         print(f"'{completed_todo}' marked as completed and removed from the list")
#
#     elif 'exit' in user_input :
#         break
#
#     else:
#         print("Invalid command")


# creating program with more efficient way

while True :
    user_input = input("Type add, show, edit, complete or exit: ")

    user_input = user_input.lower().strip()


    if user_input.startswith("add"):
        # first we read file
        if user_input[4:]== "" :
            todo = input("Enter your todo: ")
        else:
           todo = user_input[4:]


        # using with context manger

        with open("../todos.txt", "r") as file :
            existing_todos = file.readlines()


        existing_todos.append(todo+ "\n")

        with open("../todos.txt", "w") as file :
            file.writelines(existing_todos)


    elif user_input.startswith("show") :

        with open("../todos.txt", "r") as file :
            todos = file.readlines()

        # method -1
        # new_todo = []
        #
        # for item in todos:
        #     new_todo.append(item.strip("\n"))


        # method -2 (list comprehension)

        # new_todos = [item.strip("\n") for item in todos]
        # print(new_todos)

        # method 3- simple solution


        for index, todo in enumerate(todos) :
            todo = todo.strip("\n")
            print(f"{index+1}-{todo}")

    elif user_input.startswith("edit"):

        with open("../todos.txt", "r") as file :
            todos = file.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}-{todo}")

        todo_number = int(input("Which todo you want to edit?: "))
        if todo_number > len(todos):
            print("You have entered the wrong todo number")
            continue

        todo_index = todo_number - 1
        new_todo = input ("Enter new todo: ")
        todos[todo_index] = new_todo + "\n"

        with open("../todos.txt", "w") as file :
            file.writelines(todos)

        print("Todo has been edited")

    elif user_input.startswith("complete") :
        with open("../todos.txt", "r") as file:
            todos = file.readlines()

        for index, todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index + 1}-{todo}")

        completed_todo_number = int(input("Which todo you want to mark as completed?: "))
        if completed_todo_number > len(todos):
            print("You have entered the wrong todo number")
            continue

        todo_index = completed_todo_number - 1

        completed_todo = todos.pop(todo_index).strip("\n")

        with open("../todos.txt", "w") as file:
            file.writelines(todos)

        print(f"'{completed_todo}' marked as completed and removed from the list")

    elif user_input.startswith("exit") :
        break

    else:
        print("Invalid command")


