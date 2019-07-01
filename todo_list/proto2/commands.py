# commands.py
from task import Task, load_tasks, save_tasks


def list_tasks(args):
    tasks = load_tasks()
    todos = [task for task in tasks if not task.done]
    dones = [task for task in tasks if task.done]

    print('# Todo')
    for task in todos:
        print('*', task.body)
    print()
    
    print('# Done')
    for task in dones:
        print('*', task.body)


def add_task(args):
    tasks = load_tasks()
    tasks.append(Task(args.body))
    save_tasks(tasks)


def done_task(args):
    tasks = load_tasks()
    for task in tasks:
        if task.body == args.body:
            task.done = True

    save_tasks(tasks)


def clear_tasks(args):
    tasks = load_tasks()
    tasks = [task for task in tasks if not task.done]
    save_tasks(tasks)
