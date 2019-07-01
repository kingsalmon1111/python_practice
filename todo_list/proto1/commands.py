# commands.py
import argparse
from task import read_tasks, write_tasks, print_tasks, add_task, done_task, clear_done_tasks



def execute_command():
    # read tasks from json_file
    read_tasks()

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_done = subparsers.add_parser('done')
    parser_done.add_argument('task', type=str)
    parser_done.set_defaults(func=done_task)

    parser_add = subparsers.add_parser('add')
    parser_add.add_argument('task', type=str)
    parser_add.set_defaults(func=add_task)

    parser_list = subparsers.add_parser('list')
    parser_list.set_defaults(func=print_tasks)

    parser_clear = subparsers.add_parser('clear')
    parser_clear.set_defaults(func=clear_done_tasks)

    args = parser.parse_args()

    # write tasks to json_file
    write_tasks()
