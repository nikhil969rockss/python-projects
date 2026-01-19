import FreeSimpleGUI as fsg

input_label = fsg.Text("Type your todo in")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("Add")


window = fsg.Window("Todo-App", [[input_label], [input_box, add_button]])
window.read()
window.close()