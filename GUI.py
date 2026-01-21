import FreeSimpleGUI as fsg
import functions

input_label = fsg.Text("Type your todo in")
input_box = fsg.InputText(tooltip="Enter todo", key="todo-input")

todos_box = fsg.Listbox(values=functions.get_todos(), key="todos-box",
                        enable_events=True, size=(40,10))

warning_message = fsg.Text("Cannot add empty todo, Add a todo", key="warning",
                           text_color="red", font=("Helvetica", 14), visible=False)

add_button = fsg.Button("Add")

edit_button = fsg.Button("Edit")

layout = [[input_label], [input_box, add_button], [warning_message],[todos_box, edit_button]]

window = fsg.Window("Todo-App", layout=layout, font=('Helvetica', 20) )

while True:
    event, values = window.read()
    print("event-", event)
    print("values-", values)



    match event:
        case "Add":

            if values['todo-input'] == "":
                window['warning'].update(visible=True)
                continue
            window['warning'].update(value="",visible=False)

            current_todos = functions.get_todos()
            print("current-todos-----",current_todos)


            new_todo = values['todo-input'] + "\n"
            print("new todo---", new_todo)



            current_todos.append(new_todo)


            functions.write_todos(current_todos)
            window['todos-box'].update(values=current_todos)
            window['todo-input'].update(value="")


        case 'todos-box':
            selected_todo = values['todos-box'][0]
            window['todo-input'].update(value=selected_todo)

        case 'Edit':

            if values['todo-input'] == "":
                window['warning'].update(value="cannot edit empty todo",visible=True)
                continue
            window['warning'].update(value="",visible=False)



            todo_to_edit = values['todos-box'][0].replace("\n","")
            current_todos = functions.get_todos()
            current_todos = functions.remove_new_lines(current_todos)
            index = current_todos.index(todo_to_edit)

            new_todo = values['todo-input']

            current_todos[index] = new_todo

            current_todos = functions.add_new_line(current_todos)

            functions.write_todos(current_todos)
            window['todos-box'].update(values=current_todos)
            window['todo-input'].update(value="")

        case fsg.WIN_CLOSED :
            break
window.close()

