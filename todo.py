def to_do_task():
    try: 
        with open("tasks.txt","r") as fh:
            tasks=[]
            for line in fh.readlines():
                 tasks.append(line.strip())
        return tasks
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = to_do_task()

    while True:
        print("To-Do List")
        print("1.view tasks\n2.add task\n3.remove task\n4.Exit")
        choice=input("Choose an option (1/2/3/4): ")

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for t in tasks:
                    print("- " + t)
        
        elif choice == "2":
            add_task = input("Enter a new task: ")
            tasks.append(add_task)
            save_tasks(tasks)
            print("Task added successfully.")

        elif choice == "3":
            remove_task = input("Enter task name to remove: ")
            if remove_task in tasks:
                tasks.remove(remove_task)
                save_tasks(tasks)
                print("Task is removed.")
            else:
                print("Task not found.")

        elif choice == "4":
            save_tasks(tasks)
            print("Exit")
            break

        else:
            print("Invalid choice. Try again.")

main()