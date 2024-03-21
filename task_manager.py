
def reg_user():

    """
    This function will register a new user and store it in a text document: user.txt.

    Expected input:
        Username, password and confirmed password

    Return:
        Message for the user
        User data written into user.txt

    """

    with open("user.txt", "r") as user_file:
        user_data = user_file.read().split("\n")

    user_data = [i.split(";")[0] for i in user_data]
    
    # - Request input of a new username
    while True:
        new_username = input("New Username: ")

        # Ensures duplicates are created 
        if new_username in user_data:
            print("User already exists!")
        
        else:
            break


    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    if new_password != confirm_password:
        print("Passwords do no match")
        return
    
    # - If they are the same, add them to the user.txt file,
    print("New user added")
    username_password[new_username] = new_password
    
    with open("user.txt", "w") as out_file:
        user_data = []
        for k in username_password:
            user_data.append(f"{k};{username_password[k]}")
        out_file.write("\n".join(user_data))


def add_task():
    """
    Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.
    """
    
    task_username = input("Name of person assigned to task: ")

    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")


    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)

    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


def view_all():
    """
    Reads the task from task.txt file and prints to the console in a readable way.

    It will show all the attributes assocated with the task.

    """

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def view_mine():

    """
    Reads tasks that are assigned to the currently logged in user from task.txt file
    prints to the console in a very readable way

        - The user chooses a task denoted by a number
        - Choose to edit or mark as complete
        - Due date and assigned user are the only details that can be changed

    """
    

    for t in enumerate(task_list,1):
        if t[1]['username'] == curr_user:
            disp_str = f"Task: \t\t {t[1]['title']}\n"
            disp_str += f"Assigned to: \t {t[1]['username']}\n"
            disp_str += f"Date Assigned: \t {t[1]['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t[1]['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t[1]['description']}\n"
            print(disp_str)
    
    task_number = int(input("Please select a task by its corresponding number (-1 to exit): "))

    if task_number == -1:
        return
    
    task = task_list[task_number-1]

    while True:

        change_task = input("""What would you like to do with this task?
        1. Edit the task
        2. Mark as complete
        
        0. Exit back to menu
                            
        : """)

        print("\n")

        if change_task == "1":
            if task["completed"] == True:
                print("Completed tasks cannot be edited")
                return
            
            change = input("""Please select what you want to edit:
    a. assigned user
    b. due date
    
    : """).lower()
            
            print("\n")
            
            if change == "a":
                new_user = input("Enter new assigned user: ")
                task["username"] = new_user
                print(f"{new_user} as been assigned to this task.")
                return
            
            elif change == "b":
                new_due_date = input("New due date of task (YYYY-MM-DD): ")
                formatted_due_date = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                task["due_date"] = formatted_due_date
                print(f"Due date has been changed to {formatted_due_date}")
                return
            
            else:
                print("Please enter valid option.")
                

        elif change_task == "2":
            task["completed"] = True
            print(f"Task {task["title"]} has been marked as complete.")

        elif change_task == "0":
            return
        
        else:
            print("Please enter valid option.")

    

def generate_reports():

    """
    The function will generate reports of an overview of the tasks in general and the user.

    Takes data from task_list and user_passwords

    Returns two documents:

        User_overview.txt
        For each user it shows the following:
            - Total assigned tasks
            - percentage completed
            - percentage incomplete
            - perecentage overdue

        task_overview.txt
        Outputs a general report of the following:
            - number of tasks in the manager
            - number of completed tasks
            - number of incompleted tasks
            - number of overdue tasks
    
            
    """

    task_number = len(task_list)
    complete_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0


    for t in task_list:

        if t["completed"] == True:
            complete_tasks += 1

        else:
            incomplete_tasks += 1
            if t["due_date"] < datetime.now():
                overdue_tasks += 1
    
    
    
    percent_overdue = round(overdue_tasks/task_number * 100, 1)
    percent_incomplete = round(incomplete_tasks/task_number * 100,1)


    
    registered_users = len(username_password.keys())
    user_totals = []

    for user in username_password.keys():

        total_assigned = 0
        total_incomplete = 0
        total_complete = 0
        total_overdue = 0

        user_total = {
            "username": user,
            "total_assigned": 0,
            "perc_incomplete": 0,
            "perc_complete": 0,
            "perc_overdue": 0,  
        }  

        for t in task_list:

            if t["username"] != user:
                continue

            total_assigned += 1

            if t["completed"] == True:
                total_complete += 1

            else:
                total_incomplete += 1                
                if t["due_date"] < datetime.now():
                    total_overdue += 1
        
        if total_assigned > 0:

            user_total["total_assigned"] = str(total_assigned)
            user_total["perc_complete"] = str(round((total_complete/total_assigned) * 100,1))
            user_total["perc_incomplete"] = str(round((total_incomplete/total_assigned) * 100,1))
            user_total["perc_overdue"] = str(round((total_overdue/total_assigned) * 100,1))

        user_totals.append(user_total)


    # This ensures that multiple reports are appended onto the same document.
    if os.path.exists("task_overview.txt"):
        os.remove("task_overview.txt")

    if os.path.exists("user_overview.txt"):
        os.remove("user_overview.txt")

    

    with open("user_overview.txt", "w") as user_file:
        user_data_to_write = []
        columns = ["User","Assigned","Incomplete","Complete","Overdue"]
        user_data_to_write.append(";".join(columns))
        
        for t in user_totals:
            str_attrs = [
                t['username'],
                str(t['total_assigned']),
                str(t['perc_incomplete']),
                str(t['perc_complete']),
                str(t['perc_overdue'])
            ]
            
            user_data_to_write.append(";".join(str_attrs))
        user_file.write(str(registered_users))
        user_file.write("\n".join(user_data_to_write))


    
    with open("task_overview.txt", "w") as task_ov:
        columns = ["Total","Incomplete","Complete","Overdue", "Perc Incomplete", "Perc Overdue"]
        overview = [str(task_number), str(incomplete_tasks), str(complete_tasks), str(overdue_tasks), str(percent_incomplete), str(percent_overdue)]
        task_data_to_write = []

        task_data_to_write.append("; ".join(columns))
        task_data_to_write.append("; ".join(overview))
        task_ov.write("\n".join(task_data_to_write))







# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
"""
This code reads usernames and password from the user.txt file to allow a user to login.
"""

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        generate_reports()
    
    elif menu == 'ds' and curr_user == 'admin': 
        """
        If the user is an admin they can display statistics about number of users
            and tasks.
        """
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")