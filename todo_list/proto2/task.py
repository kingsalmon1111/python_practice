# task.py
import json
import os


TASKS_PATH = './tasks.json'


class Task:
    def __init__(self, body, done=False):
        self.body = body
        self.done = done


def load_tasks():
    if not os.path.exists(TASKS_PATH):
        return []

    with open(TASKS_PATH, encoding='utf-8') as f:
        data = json.load(f)
        tasks = [Task(**task) for task in data['tasks']]

    return tasks


def save_tasks(tasks):
    with open(TASKS_PATH, mode='w', encoding='utf-8') as f:
        json.dump({
            'tasks': [
                {'body': task.body, 'done': task.done}
                for task in tasks
            ]
        }, f, ensure_ascii=False, indent='  ')
