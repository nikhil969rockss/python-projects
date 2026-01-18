
# todos = []
#
# while True:
#     user_choice = input("Type 'add' or 'show' or 'exit' ")
#
#     user_choice = user_choice.lower().strip()
#
#     match user_choice :
#         case "add":
#             todo = input("Enter your todo ")
#             todos.append(todo)
#         case "show" :
#             for todo in todos:
#                 print(todo)
#
#         case "exit":
#             break
#
# print("Bye")

# adding edit functionality

todos = []

while True :
    user_input = input("Type add, show, edit, complete or exit: ")

    user_input = user_input.lower().strip()

    match user_input :
        case 'add' :
            todo = input("Enter your todo: ")
            todos.append(todo)

        case 'show' :
            for index, todo in enumerate(todos) :
                print(f"{index+1}-{todo}")

        case 'edit':
            for index, todo in enumerate(todos):
                print(f"{index + 1}-{todo}")

            todo_number = int(input("Enter todo number you want to edit: "))
            if todo_number > len(todos):
                print("You have entered the wrong todo number")
                continue

            todo_index = todo_number - 1
            new_todo = input ("Enter new todo: ")
            todos[todo_index] = new_todo
            print("Todo has been edited")

        case 'complete':
            for index, todo in enumerate(todos):
                print(f"{index + 1}-{todo}")

            completed_todo_number = int(input("Enter todo number you want to complete: "))
            if completed_todo_number > len(todos):
                print("You have entered the wrong todo number")
                continue

            todos.pop(completed_todo_number -1)
            print("Todo marked as completed")
        case 'exit' :
            break


