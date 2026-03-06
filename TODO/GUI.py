import FreeSimpleGUI as fsg
import time
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass

fsg.theme("BlueMono")

clock_label =  fsg.Text("", key="clock")

input_label = fsg.Text("Type your todo in")
input_box = fsg.InputText(tooltip="Enter todo", key="todo-input", size=(41,1))

todos_box = fsg.Listbox(values=functions.get_todos(), key="todos-box",
                        enable_events=True, size=(40,10), )

add_button = fsg.Button("Add", tooltip="add-todo", size=(10,1))

edit_button = fsg.Button("Edit", tooltip="edit-todo")

complete_button = fsg.Button("Complete", tooltip="complete-todo")

exit_button = fsg.Button("Exit")

#   To make the layout column wise
# layoutCol1 = fsg.Column([[input_label], [input_box], [todos_box]])
# layoutCol2 = fsg.Column([[add_button], [edit_button]])
#
layout = [
          [clock_label],
          [input_label, ],
          [input_box, add_button],
          [todos_box, edit_button, complete_button],
          [exit_button]
          ]



window = fsg.Window("Todo-App", layout=layout, font=('Helvetica', 20) )

while True:
    event, values = window.read(timeout=200)
    time_formate = time.strftime("%b %d %Y, %I:%M:%S %p")
    window['clock'].update(value= time_formate)

    match event:
        case "Add":

            if values['todo-input'] == "":
                fsg.popup("Cannot add empty todo",title="Error")
                continue

            current_todos = functions.get_todos()

            new_todo = values['todo-input'] + "\n"
            current_todos.append(new_todo)

            functions.write_todos(current_todos)

            window['todos-box'].update(values=current_todos)
            window['todo-input'].update(value="")


        case 'todos-box':
            try:
                selected_todo = values['todos-box'][0]
                window['todo-input'].update(value=selected_todo)
            except IndexError:
                pass

        case 'Edit':
            try:
                todo_to_edit = values['todos-box'][0].replace("\n","")
                current_todos = functions.get_todos()
                current_todos = functions.remove_new_lines(current_todos)
                index = current_todos.index(todo_to_edit)

                new_todo = values['todo-input'].replace("\n","")

                current_todos[index] = new_todo

                current_todos = functions.add_new_line(current_todos)

                functions.write_todos(current_todos)
                window['todos-box'].update(values=current_todos)
                window['todo-input'].update(value="")

            except IndexError,ValueError :
                fsg.popup("Please select a todo first",title="Error")

        case "Complete":
            try:
                todo_to_complete = values['todos-box'][0].replace("\n", "")
                all_todos = functions.get_todos()
                all_todos = functions.remove_new_lines(all_todos)
                all_todos.remove(todo_to_complete)

                all_todos = functions.add_new_line(all_todos)

                functions.write_todos(all_todos)

                window['todos-box'].update(values=all_todos)
                window['todo-input'].update(value="")


            except IndexError:
                fsg.popup("select a todo first", title="Error")

        case "Exit":
            break
        case fsg.WIN_CLOSED :
            break


window.close()


