import json
import datetime as dt

# Create a json file with a list to store all of our tasks
timedateformat = '%a, %b, %Y, %H:%M:%S %p'


def load_data(path, mode, method, source=''):
    """Function for loading and saving JSON data"""
    with open(path, mode) as file:
        if source != '':
            data = method(source, file)
        else:
            data = method(file)
        return data

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

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

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

    load_data(path=path, mode='w', method=json.dump, source=data)

    print(f"TASK CREATED: '{new_task['desc']}' | {tday} (ID: {new_id})")

def update_task(args, path):
    """Update an existing task."""

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    for task in data:
        if args.update == task['id']:    
            message = input('Update with a new description:\n')
            tday = dt.datetime.today().strftime(timedateformat).format()
            print(f"UPDATED TASK: '{message}' | {tday}")
            task['updatedAt'] = tday
            task.update({'desc': message})

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)

def delete_task(path):
    '''Delete a specified task by ID.'''

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

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
    load_data(path=path, mode='w', method=json.dump, source=data)
    

def delete_all_tasks(path):
    '''Delete ALL tasks.'''

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # Give the user the option to opt out of deleting ALL tasks.
    message = input(f"Are you sure you want to delete ALL tasks? (y/n)\n" )
    if message == 'y':
        data.clear()
        print('ALL TASKS DELETED.')
    else:
        print('ACTION CANCELLED.')  

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
    

def mark_task_in_progress(args, path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # Find a task by its ID and mark its progress
    for task in data:
        if task['id'] == args.mark_in_progress:
            task['status'] = 'In Progress'
            print(f"STATUS:'{task['desc']}': {task['status']}")

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
    

def mark_task_done(args, path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # Find a task by its ID and mark its progress
    for task in data:
        if task['id'] == args.mark_done:
            task['status'] = 'Done'
            print(f"'{task['desc']}' of status: {task['status']}")

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
    

def check_task_status(args, path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # Find a task by its ID and check its status
    for task in data:
        if task['id'] == args.status:
            print(f"'{task['desc']}' status: {task['status']}")

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
      

def list_tasks(path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # List all tasks
    print('\nCurrent tasks and their attributes:')
    for task in data:
        list_task(task)

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
    

def list_by_id(args, path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # List all tasks
    for task in data:
        if args.id == task['id']:
            list_task(task)

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
    

def list_todo_tasks(path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # List tasks by their status
    print('\nCurrent tasks and their attributes:')
    for task in data:
        if task['status'] == 'Todo':
            list_task(task)

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
    

def list_in_progress_tasks(path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # List tasks by their status
    print('\nCurrent tasks and their attributes:')
    for task in data:
        if task['status'] == 'In Progress':
            list_task(task)

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
     

def list_done_tasks(path):

    # Load the JSON file
    data = load_data(path=path, mode='r', method=json.load)

    # List tasks by their status
    print('\nCurrent tasks and their attributes:')
    for task in data:
        if task['status'] == 'Done':
            list_task(task)

    # Save changes to the JSON file
    load_data(path=path, mode='w', method=json.dump, source=data)
     
