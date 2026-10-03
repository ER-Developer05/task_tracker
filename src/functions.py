import json
import datetime as dt

# Create a json file with a list to store all of our tasks
timedateformat = '%a, %b, %Y, %H:%M:%S %p'

def list_task(task):
    '''Print the individual values of each task.'''
    print(f"\nID:             {task.get('id')}")
    print(f"Description:    {task.get('desc')}")
    print(f"Status:         {task.get('status')}")
    print(f"Created At:     {task.get('createdAt')}")
    print(f"Updated At:     {task.get('updatedAt')}")

def create_task(args, path):
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

    print(f"TASK CREATED: '{new_task['desc']}' | {tday} (ID: {new_id})")

def update_task(args, path):
    """Update an existing task."""

    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    for task in data:
        if args.update == task['id']:    
            message = input('Update with a new description:\n')
            tday = dt.datetime.today().strftime(timedateformat).format()
            print(f"UPDATED TASK: '{message}' | {tday}")
            task['updatedAt'] = tday
            task.update({'desc': message})

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def delete_task(path, testcase):
    '''Delete a specified task by ID.'''
    # Add a new task to the JSON file
    testcase = False

    with open(path, 'r') as file:
        data = json.load(file)

    # Give the user the option to opt out of deleting a task
    enter_id = int(input("\nDelete task by ID:\n"))
    if enter_id == int(enter_id):
        message = input(f"\nAre you sure you want to delete this task? (y/n)\n" )
        if message == 'y':
            for task in data:
                if enter_id == task['id']:
                    print(f"DELETED: '{task['desc']}'")
                    data.remove(task)
        else:
            print('ACTION CANCELED.')    

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)

def delete_all_tasks(path):
    '''Delete ALL tasks.'''

    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Give the user the option to opt out of deleting ALL tasks.
    message = input(f"Are you sure you want to delete ALL tasks? (y/n)\n" )
    if message == 'y':
        data.clear()
        print('ALL TASKS DELETED.')
    else:
        print('ACTION CANCELLED.')  

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def mark_task_in_progress(args, path):
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Find a task by its ID and mark its progress
    for task in data:
        if task['id'] == args.mark_in_progress:
            task['status'] = 'In Progress'
            print(f"STATUS:'{task['desc']}': {task['status']}")

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def mark_task_done(args, path):
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Find a task by its ID and mark its progress
    for task in data:
        if task['id'] == args.mark_done:
            task['status'] = 'Done'
            print(f"'{task['desc']}' of status: {task['status']}")

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def check_task_status(args, path):
    # Add a new task to the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    # Find a task by its ID and check its status
    for task in data:
        if task['id'] == args.status:
            print(f"'{task['desc']}' status: {task['status']}")

    # Save changes to the JSON file
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)   

def list_tasks(path):
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

def list_by_id(args, path):
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

def list_todo_tasks(path):
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

def list_in_progress_tasks(path):
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

def list_done_tasks(path):
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
