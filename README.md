# To-Do-List-Application-Console-Based

This is a simple console-based To-Do List application built using Python. 

It allows you to add, view, remove, and save tasks in a text file (tasks.txt).

##Features:

- View all saved tasks
  
- Add new tasks
  
- Remove existing tasks
  
- Automatically saves tasks to tasks.txt
  
- Loads tasks from the file

###Tools :Python, VS Code / terminal.

####Concepts Used: file handling, lists, functions, exception handling, and menu-driven programs.

#####Project Files:

- todo.py : Main Python script containing the program.
  
- tasks.txt : Automatically created file to store tasks.

######How to Run the Program:

1.Save the program in a file named todo.py.

2. Open terminal/command prompt.
   
3. Run the command: python todo.py

#######How it works:

Reading Tasks:

The program tries to open tasks.txt, reads each line, strips newline characters, and returns a list of tasks. If the file does not exist, it returns an empty list.

Saving Tasks:

The program writes each task into 'tasks.txt' and overwrites the file  each time to keep it updated.

########Menu Options:

1. View Tasks – Displays all current tasks.
   
2. Add Task – Prompts user to enter a new task and saves it.
   
3. Remove Task – Removes a task if it exists.
  
4. Exit – Saves tasks and exits the program.

