from functions import get_todos, write_todos
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It's", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo_index = user_action.index('add') + len('add')
        todo = user_action[todo_index:].strip()

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

        if todos == []:
            print("There is no task")
    elif user_action.startswith('edit'):
        todos = get_todos()

        number = int(user_action[5:])
        print(number)
        number = number - 1

        new_todo = input("Enter new To-do: ")
        todos[number] = new_todo + '\n'

        write_todos(todos)
    elif user_action.startswith('complete'):
        try:
            number_or_name = user_action[9:].strip()
            if number_or_name.isdigit():
                number = int(number_or_name)
            else:
                todos = get_todos()
                for index, item in enumerate(todos):
                    if item.strip('\n') == number_or_name:
                        number = index + 1
                        break
                else:
                    raise ValueError("Task not found.")

            todos = get_todos()

            index = number - 1
            todo_removed = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"Todo {todo_removed} was removed from the list.")
        except (ValueError, IndexError):
            print("Invalid input or task not found.")
    elif user_action.startswith('exit'):
        print("Bye")
        time.sleep(3)
        break
    else:
        print("Command is not valid")