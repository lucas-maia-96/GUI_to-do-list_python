import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")


window = sg.Window("My To-Do App", 
                   layout=[[label], 
                           [input_box, add_button],
                           [list_box, edit_button]], 
                   font=('Helvetica', 14))
while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
        todo_to_edit = values["todos"][0][:-1]
        new_todo = values["todo"]
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo + "\n"
        functions.write_todos(todos)
        window['todos'].update(values=todos)
    elif event =="todos":
        window["todo"].update(value=values["todos"][0])
    elif event == sg.WIN_CLOSED:
        break

window.close()
