import os
import time
os.system("clear")

print("IF TASKS ENTER IS DONE SO ENTER DONE")

def main():
    task = {}

    while True:
        user_input = input("ENTER DAILY TASK'S: ")

        if user_input.lower() == "done":
            break

        if user_input.lower() == "show":
            print(task.values())
            continue

        task.update({f"{len(task) + 1}": user_input})

    print("Tasks entered:")
    for key, value in task.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

