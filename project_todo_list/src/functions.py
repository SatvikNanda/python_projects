def get_todos():
    """Read a text file and return the list of to-do items"""
    with open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\project1_todo_list\data storage\todos.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local

#print(help(get_todos)) #printing the doc-string  

def write_todos(todos_arg):
    """Write the to-do items list in a text file"""
    with open(r'C:\Users\satvi\OneDrive\Desktop\python\udemy\project1_todo_list\data storage\todos.txt', 'w') as file:
            file.writelines(todos_arg)


if __name__ == "__main__":
     print("Hello")
     print(get_todos())