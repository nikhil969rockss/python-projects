import FreeSimpleGUI as fsg
import functions

input_label = fsg.Text("Type your todo in")
input_box = fsg.InputText(tooltip="Enter todo", key="todo-input")
add_button = fsg.Button("Add")

layout = [[input_label], [input_box, add_button]]

window = fsg.Window("Todo-App", layout=layout, font=('Helvetica', 20) )

while True:
    event, values = window.read()
    print("event-", event)
    print("values-", values)

    match event:
        case "Add":
            current_todos = functions.get_todos()
            new_todo = values['todo-input'] + "\n"
            current_todos.append(new_todo)

            functions.write_todos(current_todos)


        case fsg.WIN_CLOSED :
            break
window.close()

