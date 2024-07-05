# adding time in our codee
#created a seperate functions python file to store the functions and call them here

import time
import functions

now = time.strftime("%b %d, %Y  %H:%M:%S")

print("The current time is:", now)



while True:
    user_action = input("Type add, show, edit, complete, or exit: ")

    
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append('\n' + todo)

        functions.write_todos(todos)

    
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = functions.get_todos()

            new_todo = input("Enter a new to-do: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        
        except ValueError:
            print("Please enter a valid command:")
            continue


    
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        #todo_listcomp = [item.strip('\n') for item in todos] - this is an alternate method to do strip using list comprehension

        for index, item in enumerate(todos): #for item in todos:
            item = item.strip('\n')
            row = f"{index + 1}.{item}" #f string
            print(row)
    
    
    elif user_action.startswith('complete'):
        try:

            number = int(user_action[9:]) #when a to-do is completed we remove it from the list

            todos = functions.get_todos()

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            message = f"Todo {todo_to_remove} was completed and removed from the list."
            print(message)

            functions.write_todos(todos)
        
        except IndexError:
            print("Enter a valid index")
            continue
    
    elif user_action.startswith('exit'):
        break
    

    else :
        print("please enter the correct command")

print('Bye!')