# task.py
import json


class Task:
    todo_list = []
    done_list = []

    def __init__(self, body, done):
        self.body = body
        self.done = done


def read_tasks():
    ''' タスク一覧を読み込み、完了したタスクと未完了のタスクに仕分ける関数
    '''
    with open('./tasks.json', encoding='utf-8') as f:
        tasks = json.load(f)['tasks']
    for task in tasks:
        if not task['done']:
            Task.todo_list.append(Task(task['body'], task['done']))
        else:
            Task.done_list.append(Task(task['body'], task['done']))


def print_tasks():
    todo_list = Task.todo_list
    done_list = Task.done_list
    print('# Todo')
    for task in todo_list:
        print('*', task.body)
    print()

    print('# Done')
    for task in done_list:
        print('*', task.body)


def add_task(body):
    task = Task(body, False)
    Task.todo_list.append(task)


def done_task(body):
    done_task = None
    for task in Task.todo_list:
        body == task.body
        done_task = Task.todo_list.pop(Task.todo_list.index(task))
    if done_task:
        Task.done_list.append(done_task)
    else:
        print('「{}」はTodoに存在しません。'.format(body))


def write_tasks():
    task_list = []
    for task in Task.todo_list:
        task_list.append({'body': task.body, 'done': task.done})
    for task in Task.done_list:
        task_list.append({'body': task.body, 'done': task.done})

    with open('./tasks.json', mode='w', encoding='utf-8') as f:
        json.dump({'tasks': task_list}, f)


def clear_done_tasks():
    Task.done_list.clear()
