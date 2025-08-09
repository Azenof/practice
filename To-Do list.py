tasks=[]
def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}.{task}")
def add_task(task):
    tasks.append(task)
    print(f"\nTask '{task}' added successfully.")
def remove_task():
    if not tasks:
        print("\nNo tasks available.")
    else:
       print("\nCurrent tasks:")
       for i, task in enumerate(tasks):
           print(f"{i+1}.{task}")
       print("\nEnter task number to remove:")
       number =int(input())
       if number < 1 or number > len(tasks):
            print("\nInvalid task number.")
       else:
            removed_task=tasks.pop(number-1)
            print(f"\nTask'{removed_task}' removed successfully.")
def main():
    while True:
        print("\nchoose an option: \n1.Show Tasks.\n2.Add Task.\n3.Remove Task.\n4.Exit")
        try:
         choice=int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            show_tasks()
        elif choice==2:
            add_task(input('Enter task to add:'))
        elif choice==3:
            remove_task()
        elif choice==4:
            print("Exiting the program.")
            break
        else:
            print("invalid choice. Please try again.")
if __name__ == "__main__":
    main()


               