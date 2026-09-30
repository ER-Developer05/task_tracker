import json
from pathlib import Path
import argparse
from functions import *
import pyfiglet

# Create a json file with a list to store all of our tasks
path = Path('tasks.json')
tasks = []
if not path.exists():
    with open(path, 'w') as file:
        json.dump(tasks, file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='TASKER', usage='Add, Delete, and Manage simple tasks')
    group = parser.add_mutually_exclusive_group()
    parser.add_argument('--add',
                        metavar='STRING',
                        help="Create a new task.")
    
    parser.add_argument('--update',
                        choices=range(1,1_000_000),
                        type=int,
                        metavar='ID',
                        help="update a task.")
    
    parser.add_argument('--delete',
                        choices=['all', 'id'] ,
                        help="delete tasks.")
    
    group.add_argument('--id', 
                        type=int, 
                        help='See the details of a specific task.')
    
    parser.add_argument('--status',
                        choices=range(1,1_000_000),
                        type=int,
                        metavar='ID',
                        help='Check the status of a task')
    
    parser.add_argument('--mark-done',
                        choices=range(1,1_000_000),
                        type=int,
                        metavar='ID',
                        help='Mark a task as done')
    
    parser.add_argument('--mark-in-progress',
                        choices=range(1,1_000_000),
                        type=int,
                        metavar='ID',
                        help='Mark a task as in progress.')
    
    group.add_argument('--list',
                        choices=['all', 'todo', 'done', 'in-progress'],
                        help='List all tasks')
    
    args = parser.parse_args()

if args.add:
    create_task(args, path)
if args.id:
    list_by_id(args, path)
if args.update:
    update_task(args, path)      
if args.status:
    check_task_status(args, path)
if args.mark_done:
    mark_task_done(args, path)
if args.mark_in_progress:
    mark_task_in_progress(args, path)

if args.delete == 'id':
    delete_task(path)
elif args.delete == 'all':
    delete_all_tasks(path)

if args.list == 'all':
    list_tasks(path)
elif args.list == 'todo':
    list_todo_tasks(path)
elif args.list == 'in-progress':
    list_in_progress_tasks(path)
elif args.list == 'done':
    list_done_tasks(path)