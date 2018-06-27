import argparse
import logging
import sys

from lattec import __version__
from lattec.exceptions import LatteParserError
from lattec.parser import parse_file

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
    try:
        args = cli()

        if args.verbose:
            print(args)

        parser = parse_file(args.path.name)
        program_tree = parser.program()
    except LatteParserError as ex:
        logging.error(str(ex))
        sys.exit(1)
    except Exception as ex:
        logging.error('Unknown error')
        raise
