# 🗃️ Task Manager

Task manager program, for the purpose of viewing and managing tasks for a group of users.

**Table of Contents**

- [About the project](https://github.com/amykha/finalCapstone/edit/main/README.md#about-the-project)

  - [Built with](https://github.com/amykha/finalCapstone/edit/main/README.md#built-with)
 
- [How to navigate the program](https://github.com/amykha/finalCapstone/edit/main/README.md#how-to-navigate-the-program)
  - [Register a user](https://github.com/amykha/finalCapstone/edit/main/README.md#register-a-user)
  - [Add a new task](https://github.com/amykha/finalCapstone/edit/main/README.md#add-a-new-task)
  - [View all tasks](https://github.com/amykha/finalCapstone/edit/main/README.md#view-all-tasks)
  - [View my tasks](https://github.com/amykha/finalCapstone/edit/main/README.md#view-my-tasks)
  - [Generate reports](https://github.com/amykha/finalCapstone/edit/main/README.md#generate-reports)
  - [Display statistics](https://github.com/amykha/finalCapstone/edit/main/README.md#display-statistics)



## About the project
The project is a task manager that is accessed through logging in and is navigated through easy to read menu options. 

The program allows the user to:
- view tasks, either their own or all tasks logged in the system
- edit the tasks due date or assigned user
- create a new task
- register a new user

The project was built from a simpler version of a task manager that was refactored to extend the functionality.

## Built with
VSCode and Python


## How to navigate the program

First you will need to log in to access the manager

![loginandmenu](https://github.com/amykha/finalCapstone/assets/152326238/f3cdf98c-5622-4483-8900-982293232571)

After log in is successful the menu will appear.


### Register a user

![newuser](https://github.com/amykha/finalCapstone/assets/152326238/19bb4ba0-425d-465d-aecc-49b0c34d0dc6)

The program will prompt the user to provide a username for the new user, plus a new password and a confirmation.

If the user tries choosing a username that already exists, the bellow error message will appear:

![userexists](https://github.com/amykha/finalCapstone/assets/152326238/fbcb8636-8dd0-47c3-836e-1ed79a93234d)

Similarly, if the passwords don't match the program will produce this error message:

![passwordmatch](https://github.com/amykha/finalCapstone/assets/152326238/db5d3f02-8884-47ce-95f4-56e863fa7cd2)


### Add a new task

![newtask](https://github.com/amykha/finalCapstone/assets/152326238/089522fc-318a-4293-b08e-4892a392999c)

The program will ask for the following details:
- User that it is assigned to
- The title of the task
- Description of what needs to be done
- The date the task is due


### View all tasks

This will show a list of all tasks currently tracked by the manager with all details associated with the task.

![tasklistall](https://github.com/amykha/finalCapstone/assets/152326238/61ac8d79-9b5b-4787-a4fa-609a112fc11e)


### View my tasks

This menu option will display the tasks only assigned to the currently logged in user where they are able to manage the tasks themselves.

![viewmine](https://github.com/amykha/finalCapstone/assets/152326238/03c44391-bbd5-45ca-a7c3-a5ae879c1083)

The program will then ask the user which task they would like to manage:

![selecttasktoedit](https://github.com/amykha/finalCapstone/assets/152326238/beba025a-7c51-4384-b93b-fe25354997f5)

First option: edit the task's assigned user or due date.

![changeduedate](https://github.com/amykha/finalCapstone/assets/152326238/0178f08f-e354-4f15-82ce-77348cc30b76)

Second option: Mark the task as complete


### Generate reports

This will output two text files: user_overview.txt and task_overview.txt and save them to the same folder the program is in.

user_overview.txt
For each user, outputs a report of the following:
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


### Display Statistics

If the user is the admin they are able to select this menu option to display a simple overview.

![displaystats](https://github.com/amykha/finalCapstone/assets/152326238/38190d37-bd1b-4016-b50b-562b496bbea8)

