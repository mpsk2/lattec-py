import argparse
from lattec import __version__

__all__ = [
    'main'
]

arg_parser = argparse.ArgumentParser(description='Latte compiler', prog='lattec')
arg_parser.add_argument('path', metavar='FILE', type=argparse.FileType('r'), help='File to be compiled.')
arg_parser.add_argument('--output', '-o', dest='output', type=str, help='Output file path.')
arg_parser.add_argument('--verbose', dest='verbose', type=bool, help='Additional log output', default=False)
arg_parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + __version__)


def cli():
    args = arg_parser.parse_args()
    if args.output is None:
        name = args.path.name
        if name.endswith('.lat'):
            name = name[:-4]
        args.output = name

    return args


def main():
    arg = cli()