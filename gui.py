import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo", size=40)
add_button = sg.Button("Add", size=8, border_width=4)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[40, 10], expand_x=True)
edit_button = sg.Button("Edit", size=8, border_width=4, pad=(0, 40))
complete_button = sg.Button("Complete", size=8, border_width=4, pad=(0, 40))
exit_button = sg.Button("Exit", size=8, border_width=4, pad=4)

frist_column = [[sg.Frame('', [[clock],
                             [label],
                             [input_box, add_button],
                             [list_box],
                             [exit_button]], border_width=0)]]

edit_complete = [[sg.Frame('' , [[edit_button], [ complete_button]], border_width=0, )]]



layout = [[sg.Column(frist_column, element_justification='c'), sg.Column(edit_complete, element_justification='c')]]

window = sg.Window("My To-Do App", 
                   layout=layout, 
                   font=('Helvetica', 14))
while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    if event == "Add":
        if values['todo'] == '':
            continue
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todo'].update(value='')
        window['todos'].update(values=todos)
    elif event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item frist !", font=("Helvetica", 16))
    elif event == "todos":
        window["todo"].update(value=values["todos"][0][:-1])
    elif event == "Complete":
        try:
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item frist !", font=("Helvetica", 16))
    elif event == "Exit":
        break
    elif event == sg.WIN_CLOSED:
        break

window.close()
