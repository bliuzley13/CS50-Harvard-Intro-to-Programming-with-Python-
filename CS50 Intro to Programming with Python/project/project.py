from datetime import datetime
import os
import sys
import re

#1: Checks for list existing
def folder_existence():
    folder_name = "To-Do Lists"
    #Checks if there is that folder
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        return True
    else:
        return False

#1: Lists files in the folder
def list_files_in_folder(folder_name):
    #Makes a list for the running program
    files = [file for file in os.listdir(folder_name) if file.endswith('.txt')]
    return files

#1: Opens file
def load_text_file(file_path):
    try:
        #Lets you see what is in the file in the terminal
        with open(file_path, "r") as file:
            content = file.read()
            print(f"Contents of '{file_path}':\n\n{content}")
    except FileNotFoundError:
        print("File not found.")

#1: Chooses the file to load
def choose_file_to_load(folder_name):
    files = list_files_in_folder(folder_name)
    #Checks if there are no text files
    if not files:
        print("There are no text files found.")
        return
    #Numbers the text files available that exist
    print("Here are the available text file(s):")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")
    #Lets you choose which text file to choose
    file_choice = input("\nWhat is the number of the file you want to load?: ")
    while not file_choice.isdigit():
        print("Invalid input. Please enter a number.")
        file_choice = input("\nWhat is the number of the file you want to load?: ")
    #Lets you make the choice of the text file
    choice = int(file_choice)
    while not 1 <= choice <= len(files):
        print("Invalid choice. Please enter a valid file number.")
        file_choice = input("What is the number of the file you want to load?: ")
        choice = int(file_choice)
    #Goes to the method to see the contents of the chosen file
    chosen_file = files[choice - 1]
    file_path = os.path.join(folder_name, chosen_file)
    load_text_file(file_path)

def get_acknowledge(acknowledge):
    #Lets you exit out of going forward with your list
    while True:
        if acknowledge == "1":
            return True
        elif acknowledge == "0":
            return False
        else:
            return "unknown"


def get_priority(priority):
    #Main code that can be referenced to create a reference in a list
    while True:
        if priority == "0":
            priority = "nothing"
            return priority
        try:
            priority = int(priority)
            if priority <= 0:
                priority = input("Enter Priority Level (1, 2, 3, etc...):  ")
            else:
                break
        except ValueError:
            print(f"Invalid input. The input must be a number greater than 0.")
            priority = input("Enter Priority Level (1, 2, 3, etc...):  ")

    return priority

def get_task(task):
    #Main code that can be referenced to create a task
    while True:
        if task == "0":
            task = "nothing"
            return task
        if not task.strip():  # Checks if the task input is not empty after removing leading/trailing spaces
            print("Task cannot be empty. Please enter a valid task.")
            task = input("\nEnter your task: ")
        else:
            break
    return task

def get_time(time):
    #Main code that can be used to check if a time is a certain format
    while True:
        if time == "0":
            time = "nothing"
            return time
        if len(time) == 4 and time[1] == ":":
            time = "0" + time
        if time.isdigit():
            if len(time) == 2 and int(time) < 60:
                time = "00:" + time
            if len(time) == 1 and int(time) < 10:
                time =  "00:0" + time
        if not time:
            time = "00:00"
            break
        # Check if the time format matches hh:mm using regular expressions
        if re.match(r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$', time):
            break
        else:
            print("Invalid time format. Please enter time in 'hh:mm' format.")
            time = input("Enter your expected time (hh:mm, h:mm, mm, m): ")
    return time

#2: main list creator
def create_new_list():
    tasks = []

    #Lets you choose if you change your mind to exit the program
    acknowledge = input("\nPlease press 1 to Proceed, or 0 to cancel: ")
    while True:
        result_acknowledge = get_acknowledge(acknowledge)
        if result_acknowledge == True:
            break
        elif result_acknowledge == False:
            return
        else:
            print("Invalid choice. Please try again.")
            acknowledge = input("\nPlease press 1 to Proceed, or 0 to cancel: ")

    print("Note: You may press 0 to exit out of either inputting the priority, task, and time.")
    #Does the checks continuously
    while True:

        task = input("\nEnter your task: ")
        task = get_task(task)
        if task == "nothing":
            break
        priority = input("Enter Priority Level (1, 2, 3, etc...):  ")
        priority = get_priority(priority)
        if priority == "nothing":
            break
        time = input("Enter your expected time (hh:mm, h:mm, mm, m): ")
        time = get_time(time)
        if time == "nothing":
            break

        #Not wanting to continue with the code
        tasks.append((priority, task, time))
        #Writes out the task which was just added
        print("\nAdded Task: --> Priority-", str(priority), ":", str(task), "- " + str(time))
        #Writes out the tasks already added
        print("\nCurrent number of tasks that you have added")
        for index, (priority, task, time) in enumerate(tasks, start=1):
            print(f"{index}. Priority-{priority}: {task} - {time}")
        #Choice to add another task
        choice = input("\nWould you like to add another task? (y/n): ")
        while choice.lower() not in ('y', 'n'):
            choice = input("Invalid input. Please enter 'y' or 'n': ")
        #Lets you not add another task if wished so
        if choice.lower() == 'n':
            # Check if tasks are empty or contain only one task
            if not tasks:
                print("No tasks added.")
                return

            #Lets you see your list
            prev_choice = input("Would you like to preview your current list? (y/n): ")
            while prev_choice.lower() not in ('y', 'n'):
                prev_choice = input("Invalid input. Please enter 'y' or 'n': ")
            if prev_choice.lower() == 'y':
                print("\n")
                print(create_preview(tasks))
                #Asks to modify tasks after seeing your tasks
            modify_tasks = input("Would you like to modify your tasks? Modifying your tasks mean adding, deleting, or editing to them. Please enter (y/n): ")
            while modify_tasks.lower() not in ('y', 'n'):
                modify_tasks = input("Invalid input. Please enter 'y' or 'n': ")

            if modify_tasks.lower() == 'y':
                tasks = modify_list(tasks)
                #Reorders if there is more than 1 task

            reorder_tasks(tasks)
            #Lets you save the tasks into the program if you are satisfied
            print(create_preview(tasks))
            save_choice = input("Would you like to save this list? (y/n): ")
            while save_choice.lower() not in ('y', 'n'):
                save_choice = input("Invalid input. Please enter 'y' or 'n': ")
            if save_choice.lower() == 'y':
                save_to_text_file(create_preview(tasks))
            return

#2: Reorders Tasks
def reorder_tasks(tasks):
    if len(tasks) == 1:
        return
    reorder_choice = input("Would you like to reorder tasks by time? (least to max/most to least) (y/n): ")
    while True:
        #Asks the first question to reorder the tasks
        while reorder_choice.lower() not in ('y', 'n'):
            reorder_choice = input("Invalid input. Please enter 'y' or 'n': ")
        #Asks by the time intended to reorder
        if reorder_choice.lower() == 'y':
            sort_key = input("Sort by least to max or most to least? (l/m): ")
            while sort_key.lower() not in ('l', 'm'):
                sort_key = input("Invalid input. Please enter 'l' or 'm': ")

            # Reorder tasks by time within each priority
            sorted_tasks = {}
            for p in set(task[0] for task in tasks):
                tasks_by_priority = [(priority, task, time) for priority, task, time in tasks if priority == p]
                if sort_key.lower() == 'l':
                    sorted_tasks[p] = sorted(tasks_by_priority, key=lambda x: x[2])  # Sort by time
                else:
                    sorted_tasks[p] = sorted(tasks_by_priority, key=lambda x: x[2], reverse=True)  # Sort by max time

            # Display reordered tasks
            sort_message = "least to max" if sort_key.lower() == 'l' else "most to least"
            print(f"\nReordered tasks (sorted by {sort_message} time):")
            for priority, ordered_tasks in sorted(sorted_tasks.items()):
                print(f"Priority {priority}:")
                for index, (priority, task, time) in enumerate(ordered_tasks, start=1):
                    print(f"{index}. {task} - {time}")
            #Asks to reorder if wished
            reorder_choice = input("Would you like to reorder tasks again? (y/n): ")
            if reorder_choice.lower() == 'n':
                break  # Exit the reordering loop if the user doesn't want to continue
        else:
            break  # Exit the reordering loop if the user chooses not to reorder

#2: Gives a preview of the list made
def create_preview(tasks):
    preview = {}
    for (priority, task, time) in tasks:
        if priority not in preview:
            preview[priority] = []
        preview[priority].append((task.capitalize(), time))

    # Construct and return the preview string
    preview_str = ""
    for priority, tasks in sorted(preview.items()):
        if int(priority) >= 10:
            preview_str += f"'-------------Priority-{priority}--------------'\n"
        else:
            preview_str += f"'-------------Priority-{priority}---------------'\n"
        for index, (task, time) in enumerate(tasks, start=1):
            preview_str += f"{index}. {task.ljust(30)} {time}\n"
        preview_str += "\n"

    return preview_str

#2: Adds, Deletes, or Edits tasks with the option of doing nothing
def modify_list(tasks):
    while True:
        modify_choice = input("Would you like to modify tasks? (a as add, d as delete, e as edit, or n as neither): ")
        if modify_choice.lower() == "a":
            # Add a new task with referencing previous methods
            task = input("\nEnter your task: ")
            task = get_task(task)
            if task == "nothing":
                break
            priority = input("Enter Priority Level (1, 2, 3, etc...):  ")
            priority = get_priority(priority)
            if priority == "nothing":
                break
            time = input("Enter your expected time (hh:mm, h:mm, mm, m): ")
            time = get_time(time)
            if time == "nothing":
                break

            tasks.append((priority, task, time))
            print("Task added.")

        elif modify_choice.lower() == "d":
            # Delete a task
            # Checks if there are any tasks that could be deleted
            if not tasks:
                print("There are no tasks to delete.")
                continue
            #If there are tasks worth deleting
            else:
                print("Current tasks:")
                for index, (priority, task, time) in enumerate(tasks, start=1):
                    print(f"{index}. Priority-{priority}: {task} - {time}")

                while True:
                    try:
                        delete_index = int(input("What is the number of the task you want to delete?: "))
                        if 1 <= delete_index <= len(tasks):
                            del tasks[delete_index - 1]
                            print("Task deleted.")
                            break
                        else:
                            print("Invalid task number. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        elif modify_choice.lower() == "e":
            # Edit a task
            # Does not do anything if there are no tasks to edit
            if not tasks:
                print("There are no tasks to edit.")
                continue
            # If there are tasks to edit
            else:
                print("Current tasks:")
                for index, (priority, task, time) in enumerate(tasks, start=1):
                    print(f"{index}. Priority-{priority}: {task} - {time}")

                while True:
                    try:
                        edit_index = int(input("Enter the number of the task to edit: "))
                        if 1 <= edit_index <= len(tasks):
                            task = input("\nEnter your modified task: ")
                            task = get_task(task)
                            if task == "nothing":
                                break
                            priority = input("Enter Priority Level (1, 2, 3, etc...):  ")
                            priority = get_priority(priority)
                            if priority == "nothing":
                                break
                            time = input("Enter your expected time (hh:mm, h:mm, mm, m): ")
                            time = get_time(time)
                            if time == "nothing":
                                break

                            tasks[edit_index - 1] = (priority, task, time)
                            print("Task edited.")
                            break
                        else:
                            print("Invalid task number. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

        elif modify_choice.lower() == "n":
            return
        else:
            print("Invalid choice. Please enter 'a' to add, 'd' to delete, or 'n' for neither.")

        # Display a preview of modified tasks after each modification
        print("\nModified Tasks Preview:")
        print(create_preview(tasks))  # Display modified tasks as a preview

    return tasks

#2: Saves List
def save_to_text_file(content):
    # Uses datetime to create a premade name
    now = datetime.now()
    default_name = now.strftime("%m-%d-%Y_%H-%M") + "_Auto_List"
    # Option to name the list
    folder_name = "To-Do Lists"
    file_name = input(f"How do you want to name your list?: ")
    if not file_name:
        file_name = default_name
    # Allows to save the text file
    file_path = f"{folder_name}/{file_name}.txt"
    with open(file_path, "w") as file:
        file.write(content)
    print(f"Your list is saved in the To-Do Lists folder.")


#3: Deletes List
def delete_existing_list(folder_name):
    files = list_files_in_folder(folder_name)
    # Checks if there are any files to delete
    if not files:
        print("There are no text files found.")
        return
    # Shows the available text files to delete
    print("Here are the available text file(s) you can delete:")
    for index, file in enumerate(files, start=1):
        print(f"{index}. {file}")
    # Lets you choose which file to delete
    while True:
        try:
            choice = int(input("\nWhat is the number of the file to delete (Press 0 to cancel): "))
            if 1 <= choice <= len(files):
                chosen_file = files[choice - 1]
                file_path = os.path.join(folder_name, chosen_file)
                os.remove(file_path)
                print(f"Your file '{chosen_file}' is now deleted.")
                break
            elif choice == 0:
                break
            else:
                print("Invalid choice. Please enter a valid file number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#4: Deletes folder if it is empty
def delete_empty_folder(folder_name):
    if not os.listdir(folder_name):
        os.rmdir(folder_name)
        print(f"\nYour folder '{folder_name}' is empty so it is deleted.")


def main():
    #Welcomes the User
    print("\nWelcome to the To-Do List App.")

    #Creates folder if it does not exist in the program
    if folder_existence() == False:
        os.makedirs("To-Do Lists")

    while True:
        print("\nHow may we help you today?")
        print("1. Load Pre-Made List")
        print("2. Create New List")
        print("3. Delete Existing List")
        print("4. Exit Program")

        #Initial Choice
        init_choice = input("\nEnter your choice (1-4): ")
        if init_choice == "1":
            #Loads Pre-Made List
            #Checks if the folder is empty
            if os.listdir("To-Do Lists") == False:
                print("There is no list present.")
            choose_file_to_load("To-Do Lists")
        elif init_choice == "2":
            #Creates the New List
            print('We will now create your list.')
            create_new_list()
        elif init_choice == "3":
            #Deletes Existing List
             #Checks if the folder is empty
            if os.listdir("To-Do Lists") == False:
                print("There is no list present.")
            else:
                delete_existing_list("To-Do Lists")
        elif init_choice == "4":
            #Exits Program
            if os.listdir("To-Do Lists") == []:
                delete_empty_folder("To-Do Lists")
            print("Have a Nice Day!")
            sys.exit("\nProgram Exited Successfully\n")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()