FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath,'r') as file:
        todos_local = file.readlines()
    return todos_local

def writetodo(content, filepath=FILEPATH):
    with open(filepath,'w') as file:
        file.writelines(content)

if __name__ == '__main__':
    print(get_todos())