import functions
import PySimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter to-do", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(),
                       key="todos", enable_events=True, size=(20, 10))
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")

window = gui.Window("My To-Do_App",
                    layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
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
            print(index)
            todos[index] = new_todo.title()
            functions.write_todos(todos)
            # listbox instance key="todos"
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case gui.WIN_CLOSED:
            break

window.close()
