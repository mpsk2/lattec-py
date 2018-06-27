import argparse

__all__ = [
    'cli'
]

arg_parser = argparse.ArgumentParser(description='Latte compiler')
arg_parser.add_argument('path', metavar='FILE', type=argparse.FileType('r'), help='File to be compiled.')
arg_parser.add_argument('--output', '-o', dest='output', type=str, help='Output file path.')


def cli():
    args = arg_parser.parse_args()
    if args.output is None:
        name = args.path.name
        if name.endswith('.lat'):
            name = name[:-4]
        args.output = name

    return args