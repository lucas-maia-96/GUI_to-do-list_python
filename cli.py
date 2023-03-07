from modules import functions
import time

now = time.strftime("%d/%m/%Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    
    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'
        list_todos = functions.get_todos()
        list_todos.append(todo) 
        functions.write_todos(list_todos)
        
    elif user_action.startswith("show"):
        list_todos = functions.get_todos()
        new_Todos = [item.strip('\n') for item in list_todos]
        print()
        for index, item in enumerate(new_Todos):
            print(f"{index+1}-{item.capitalize()}")
        print()
        
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1
            new_todo = input("Enter the new todo: ") + '\n'
            list_todos = functions.get_todos()
            list_todos[number] = new_todo 
            functions.write_todos(list_todos)
        except ValueError: 
            print("Your command is not valid")
            continue
        
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:]) -1
            list_todos = functions.get_todos()
            ex_todo = list_todos.pop(number).strip('\n')
            functions.write_todos(list_todos)
            print(f"Todo '{ex_todo}' was removed from the list")
            print()
        except IndexError:
            print("There is no item with that number")
        
    elif user_action.startswith("exit"):
        break
    else:
        print("Hey, this command is not valid")
            
            
            