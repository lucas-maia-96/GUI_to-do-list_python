import functions
import PySimpleGUI as sg
import time

image_add = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAABigAwAEAAAAAQAAABgAAAAAEQ8YrgAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDYuMC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KGV7hBwAAAnJJREFUSA2dlbuPTVEUh93BDdFIVBKZSZTKiUZiSAalP4FcMyRqnUapMn+AiMajUaCgHR2dQT2JURCvwiOEeH7fued3su9x7ris5Dt77bX3Xq+zz729Df8uGzkiXfIL43dw/C+ZmvBUL/saJYZ1Rp3/hL2wCJshmepHHsJl+FLPs850fUlLDrDtFXhwHDdZS6UTFVA6f1s7/soo9vsjLID7lsDAp0HZNBzGP7ucf2O7Tn7U4+PiuA5ds01KP6UMp6NP13RiWyx7B5hxskr5M9jmQRlUz2GQWu0ekvkcy2lLMjfD4EtXfwdWYrucXwKlPxxGn8lQ52/AA13O20Gc5xtoAsQZa5WYuZt0fgvabcE0Ijq1ilRiS7dC2tf0E1t1tdwwrufuiehYJ2JSaSlqJVZcSSrwhZrFJM7dl8uxgn4N7sN72An7YRkUu9FE9wt9CWY3rudW6LrOToKyDaZhN+yCVJMkmjd9kUUP+wE5tjHzOPcdKcfhASTwJ/S7cAQaScSjWLIxYzuI82R+Ab1rPbYB642knBNYsqEMkuz9MVPM3H2f63GZ8TCsQdrr+Vn4QxawJIgvST3jGXR7bluyx/EGKC+gtF+trPUj185pu5IE2MfaNKS6e+g6PwXKebgOT8BAz2FExgXJi9/Dbm9LsjxUnN5S6GfrPR8KW6OWQcp26XQevIreFudrYFvMXLkDTyE/Masau6QMYrvy4s6he+u8igaI3bYoOteeFi7lirrYFoMoj8BfSsu9Dc/ADI/BFES2oxwEW6X9NSzCX6V04ubMB+jJ1KxL/Fudg4nFSvsQ5zk4i3IFvC3+F9hzP0BvmtL7Da+J6PwkF1grAAAAAElFTkSuQmCC'
sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit", size=10)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=10 )

window = sg.Window("My To-Do App", 
                   layout=[[clock], 
                           [label], 
                           [input_box, add_button],
                           [list_box, edit_button, complete_button], 
                           [exit_button]], 
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
