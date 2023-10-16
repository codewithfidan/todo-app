import functions
import time

now = time.strftime("%B %d %Y, %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.title()+"\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):

        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter a todo: ").capitalize().strip()
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("You should enter a number of todo that you want to edit.")
            continue

    elif user_action.startswith("complete"):

        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove} is deleted.")
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print("You should enter a number of todo that you want to complete.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye:)")

