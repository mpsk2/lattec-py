import argparse
import logging
import sys

from lattec import __version__
from lattec.exceptions import LatteParserError
from lattec.parser import parse_file
from lattec.validations.validate import validate

__all__ = [
    'main',
    'main_f',
]

arg_parser = argparse.ArgumentParser(description='Latte compiler', prog='lattec')
arg_parser.add_argument('path', metavar='FILE', type=argparse.FileType('r'), help='File to be compiled.')
arg_parser.add_argument('--output', '-o', dest='output', type=str, help='Output file path.')
arg_parser.add_argument('--verbose', dest='verbose', type=bool, help='Additional log output', default=False)
arg_parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + __version__)
arg_parser.add_argument('--validation-only', action='store_true', help='Run only validations')


def cli():
    args = arg_parser.parse_args()
    if args.output is None:
        name = args.path.name
        if name.endswith('.lat'):
            name = name[:-4]
        args.output = name

    return args


def compile_latte(program_tree):
    raise NotImplementedError('compile')


def main_f():
    args = cli()

    if args.verbose:
        print(args)

    parser = parse_file(args.path.name)
    program_ctx = parser.program()

    validate(program_ctx)
    compile_latte(program_ctx)


def main():
    try:
        main_f()
    except LatteParserError as ex:
        logging.error(str(ex))
        sys.exit(1)
    except Exception as ex:
        logging.error('Unknown error')
        raise
