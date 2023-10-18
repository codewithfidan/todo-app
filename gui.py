import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter to-do", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(),
                       key="todos", enable_events=True, size=(44, 10))
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]]
window = gui.Window("My To-Do_App", layout=layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"].title() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()

            index = todos.index(todo_to_edit)

            todos[index] = new_todo.title()
            functions.write_todos(todos)
            window["todos"].update(values=todos)  # listbox instance key="todos"
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"] .update(value="")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break

window.close()
