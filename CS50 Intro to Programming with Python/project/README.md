#To-Do List Application
#### Video Demo: https://youtu.be/CGvP6wZ-YbY
#### Description:

This project entails a To-Do List App designed to help a consumer make their tasks sorted by importance as priority. The tasks are numbered from top to bottom for each priority, which can be sorted based on time. The time can be sorted from the least to most and most to least based on the preference of the user. The tasks in each priority can be edited to move around through each priority one by one. These tasks can be added or deleted. Tasks can be viewed in the specific format that they will be saved in. The saved tasks are in a text file within a folder made when the program first runs. That folder will be deleted automatically if there are no files within it when the program is existed. As for the text file containing the tasks, the viewer can view it formally through the program. The text file can be deleted as well. The list is saved by default with a naming scheme which uses the date and time. The user has the option to choose a name for that list to their liking if they are not satisfied with that name. There are aesthetic aspects which appeal to the user's experience. Print statements help explain to the user what to expect and what they can do to navigate through the program. There is a menu based system when the program first runs to allow the user to choose their decision. We have an example text file below with a list of each method and explanation of everything which was developed throughout the project.


TODO
#### Current Tasks
None

DONE
#### Implement main
1. Load List                - Opens List already saved in folder
2. Create List              - Creates a list that can be sorted and saved
3. Delete List              - Deletes a list within the folder
4. Exit Program             - Exits the program

#### Implement functions (a is a placeholder for what enters that method)
1.  folder_existence()      - Checks if "To-Do Lists" folder exists
2.  list_files_in_folder(a) - Shows the list text files that exist
3.  load_text_file(a)       - Opens the text file
4.  choose_file_to_load(a)  - Choosing the file to Load Selection
5.  get_acknowledge()       - Exists to back out of making the list if needed
6.  get_priority()          - Allows a priority level inputted for the list
7.  get_task()              - Allows a task that is inputted for the list
8.  get_time()              - Allows a time that is inputted for the list
9.  create_new_list()       - Makes the main list that can be saved
10. reorder_tasks(a)        - Reorders the tasks by time
11. create_preview(a)       - Creates a preview of the tasks
12. modify_list(a)          - Modifies the list if need be
13. saves_to_text_file(a)   - Saves the list to a text file
14. delete_existing_list(a) - Deletes an existing list
15. delete_empty_folder(a)  - Deletes the folder if it is empty


#### In main, these require certain functions to serve their purpose
1. Load List
2. Create List
3. Delete List

#### Completed Tasks
1. Imported correct packages
2. Working Main Code
3. Implemented Methods

#### List of Functionality
1. User-Friendly Features
    1. Print Statements - Explain to the User what is happening
    2. Input Requirements - To smoothly run the program
    3. To-Do List Folder - To access lists saved for later
    4. View List - Before it is saved
2. Comments to Understand for Future Reference
3. Features
    1. Checks if a folder exists
    2. Creates a list of To-Do lists to view for later
    3. Opens a file to view in the terminal
    4. Simple function to continue making list
    5. Task Inputting with restraints
        1. 0 for each to exit making the task
        2. Loops until desired input type is made
        3. Priority requires int
        4. Task requires anything but just can not be empty
        5. Time requires hours and minutes in multiple forms
    6. Shows added task and tasks added within that session
    7. Asks to add another task
    8. Asks to reorder tasks by time (least to most) or (most to least)
    9. Asks to show a preview before saving
        1. Format for Priority which are categories
        2. Tasks which are in each category that can be reordered
    10. Asks to modify the tasks
        1. Adds a task
        2. Deletes a task
        3. Edits a task
        4. Does nothing, exits the code
    11. Asks to save tasks in a text file
        1. Uses datetime to create default text file name
        2. Saves text file in folder
    12. Deletes a list
    13. Deletes the folder if empty when exiting the program
4. Code-Fixes
    1. Repeated asking until acceptable input
    2. Base inputs
    3. Certain elements being empty
    4. Placeholders and Loops to continue the program until exited

#### MOVING FORWARD - POSSIBLE IMPROVEMENTS TODO
1. Implementing further functions to reduce redundancy
2. Implementing modifying the list after it is saved into a text file
3. Reordered Tasks before Saved List

#### Sample Text File - example.txt
'-------------Priority-1---------------'
1. Groceries                      01:30
2. Cs assignment                  01:45
3. Dishwashing                    00:45
4. Text emergency                 00:05

'-------------Priority-2---------------'
1. Restock bathroom               00:15
2. Take out trash                 00:30
3. Clean headphones               00:20

'-------------Priority-3---------------'
1. Laundry                        02:00
2. Modify project                 00:50
3. Bird sketch                    02:30

'-------------Priority-4---------------'
1. Pack for trip                  04:00
2. New playlist                   01:30
3. Clean desk space               00:45

'-------------Priority-10--------------'
1. Econ project                   12:35
2. Design game                    15:00