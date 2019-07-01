import argparse

from commands import list_tasks, add_task, done_task, clear_tasks


def main():
    parser = argparse.ArgumentParser()
    sub_parsers = parser.add_subparsers()

    list_parser = sub_parsers.add_parser('list', help='display a list of the tasks')
    list_parser.set_defaults(func=list_tasks)

    add_parser = sub_parsers.add_parser('add', help='add a task')
    add_parser.add_argument('body', type=str, help='body of the task to be added')
    add_parser.set_defaults(func=add_task)

    done_parser = sub_parsers.add_parser('done', help='complete the task')
    done_parser.add_argument('body', type=str, help='body of the task to be completed')
    done_parser.set_defaults(func=done_task)

    clear_parser = sub_parsers.add_parser('clear', help='clear all completed tasks')
    clear_parser.set_defaults(func=clear_tasks)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
