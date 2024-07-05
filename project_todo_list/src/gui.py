import functions
import FreeSimpleGUI as fsg
import time


fsg.theme("TealMono")
clock = fsg.Text('', key='clock')

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter to-do", key='todo')
add_button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45, 10])
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")


window = fsg.Window('My to-do list App', 
                    layout=[[clock],
                            [label],
                            [input_box, add_button], 
                            [list_box, edit_button, complete_button],
                            [exit_button]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y  %H:%M:%S"))
    print(event)
    print(values)

    match event:    
        case "Add":
            todos = functions.get_todos() #make a list variable todos which calls and stores the todos in the text file
            new_todo = values['todo'] + "\n" #new_todo variable stores whatever value is there in the todo key
            todos.append(new_todo) #in the above list the new todo is added
            functions.write_todos(todos) #the new list is rewritten

            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0] #the value will be in the todos key
                new_todo = values['todo'] #new_todo will be in the todo key

                todos = functions.get_todos()#making a list
                index = todos.index(todo_to_edit)#finding the index in the list
                todos[index] = new_todo #updating the todo

                functions.write_todos(todos)

                window['todos'].update(values=todos)
            
            except IndexError:
                fsg.popup("Please select an item first.", font=('Helvetica', 20)) #when user clicks edit without selecting an item

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()

                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update("")
            except IndexError:
                fsg.popup("Please select an item first.", font=('Helvetica', 20))

        case "Exit":
            break
        
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case fsg.WIN_CLOSED: #for quitting the application
            break

window.close()