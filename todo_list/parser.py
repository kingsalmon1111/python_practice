import argparse


parser = argparse.ArgumentParser()
parser.add_argument('command', type=str)

subparsers = parser.add_subparsers()

parser_add = subparsers.add_parser('add')
parser_add.add_argument('task', type=str)

parser_done = subparsers.add_parser('done')
parser_done.add_argument('task', type=str)

parser_list = subparsers.add_parser('list')

parser_clear = subparsers.add_parser('clear')


args = parser.parse_args(['add', 'add', 'add'])

print(args)
