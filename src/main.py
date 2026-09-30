import json
from pathlib import Path
import argparse
import datetime as dt

# Create a json file with a list to store all of our tasks
path = Path('tasks.json')
timedateformat = '%a, %b, %Y, %H:%M:%S %p'
tasks = []
if not path.exists():
    with open(path, 'w') as file:
        json.dump(tasks, file)

def list_task(task):
    '''Print the individual values of each task.'''
    print(f"\nID:    {task.get('id')}")
    print(f"Description:    {task.get('desc')}")
    print(f"Status:    {task.get('status')}")
    print(f"Created At:    {task.get('createdAt')}")
    print(f"Updated At:    {task.get('updatedAt')}")

def create_task():
    """Create a new task"""

    # Add a new task
    desc = args.add

    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Add a unique ID to each newly created task.
    highest = 0
    for task in data:
        if task['id'] > highest:
            highest = task['id']
    new_id = highest + 1

    # Create a new task
    tday = dt.datetime.today().strftime(timedateformat).format()
    new_task = {'id': new_id,
                'desc': desc,
                'status': 'Todo',
                'createdAt': tday,
                'updatedAt': 'No updates'}
    
    data.append(new_task)

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"New task '{new_task['desc']}' added at: {tday} (ID: {new_id})")

def update_task():
    """Update an existing task."""

    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    for task in data:
        if args.id == task['id']:    
            tday = dt.datetime.today().strftime(timedateformat).format()
            print(f"Updating task '{args.update}' at: {tday}")
            task['updatedAt'] = tday
            task.update({'desc': args.update})

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def delete_task():
    '''Delete a specified task by ID.'''
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Give the user the option to opt out of deleting a task
    message = input(f"Are you sure you want to delete this task? (y/n)\n" )
    if message == 'y':
        for task in data:
            if args.id == task['id']:
                print(f"Task Deleted: '{task['desc']}'")
                data.remove(task)
    else:
        print('Action canceled')    

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def delete_all_tasks():
    '''Delete ALL tasks.'''

    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Give the user the option to opt out of deleting ALL tasks.
    message = input(f"Are you sure you want to delete ALL tasks? (y/n)\n" )
    if message == 'y':
        data.clear()
        print('All Tasks Deleted.')
    else:
        print('Action canceled')  

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def mark_task_in_progress():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Find a task by its ID and mark its progress
    for task in data:
        if task['id'] == args.id:
            task['status'] = 'In Progress'
            print(f"Status of '{task['desc']}': {task['status']}")

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def mark_task_done():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Find a task by its ID and mark its progress
    for task in data:
        if task['id'] == args.id:
            task['status'] = 'Done'
            print(f"Status of '{task['desc']}': {task['status']}")

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def check_task_status():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Find a task by its ID and check its status
    for task in data:
        if task['id'] == args.id:
            print(f"Status of '{task['desc']}': {task['status']}")

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def list_tasks():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # List all tasks
    print('\nCurrent tasks and their attributes:')
    for task in data:
        list_task(task)

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def list_by_id():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # List all tasks
    for task in data:
        if args.id == task['id']:
            list_task(task)

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def list_todo_tasks():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # List tasks by their status
    print('\nCurrent tasks and their attributes:')
    for task in data:
        if task['status'] == 'Todo':
            list_task(task)

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def list_in_progress_tasks():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # List tasks by their status
    print('\nCurrent tasks and their attributes:')
    for task in data:
        if task['status'] == 'In Progress':
            list_task(task)

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def list_done_tasks():
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # List tasks by their status
    print('\nCurrent tasks and their attributes:')
    for task in data:
        if task['status'] == 'Done':
            list_task(task)

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Use Task Tracker to Add, Update, and Delete tasks!')
    parser.add_argument('--add', 
                        help="Add a new task and set it's description after the command.")
    
    parser.add_argument('--update', 
                        help="Update a task by adding a string after the command")
    
    parser.add_argument('--delete', 
                        action='store_true', 
                        help="Delete a single task by typing --id, the cooresponding task id, then --delete, or delete ALL tasks by simply calling the command")
    
    parser.add_argument('--id', 
                        type=int, 
                        help='Get the ID of an existing task')
    
    parser.add_argument('--status',
                        help='Check the staus of a task',
                        action='store_true')
    
    parser.add_argument('--mark_done',
                        help='Mark a task as done',
                        action='store_true')
    
    parser.add_argument('--mark_in_progress',
                        help='Mark a task as in progress',
                        action='store_true')
    
    parser.add_argument('--list',
                        choices=['all', 'todo', 'done', 'in-progress'],
                        help='List all tasks')
    
    args = parser.parse_args()

if args.add:
    create_task()

if args.id:
    list_by_id()
elif args.id and args.update:
    update_task()
elif args.id and args.delete:
    delete_task()
elif args.delete:
    delete_all_tasks()

if args.status and args.id:
    check_task_status()

if args.mark_done and args.id:
    mark_task_done()

if args.mark_in_progress and args.id:
    mark_task_in_progress()

if args.list == 'all':
    list_tasks()
elif args.list == 'todo':
    list_todo_tasks()
elif args.list == 'in-progress':
    list_in_progress_tasks()
elif args.list == 'done':
    list_done_tasks()