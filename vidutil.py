import argparse as ap
import os
import sys
from importlib import import_module
from traceback import format_exc

sys.path.insert(0, f'{os.path.dirname(__file__)}/scripts')

# Initialize
# Compatiblilty with PyOne
argv = sys.argv
if len(argv) >= 2:
    if argv[0] == argv[1]:
        argv = argv[1:]


def dump():
    # Masks full file paths to the `.py` files.
    traceback = format_exc().splitlines()
    for index, line in enumerate(traceback):
        if '  File' == line[0:6]:
            x, y = line.split('  File')[1].strip().split(',', 1)
            x, y = os.path.split(x.strip('"'))[1], y.strip()
            traceback[index] = f'  File "{x}", {y}'
    with open(f'{os.path.dirname(__file__)}/traceback.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(traceback))


def main():
    parser = ap.ArgumentParser()
    parser.add_argument('-s', '--script',
                        help='Script to run.',
                        nargs=1, action='store', required=True, metavar='Script')

    parser.add_argument('-v',
                        '--videos',
                        help='Input video file(s).',
                        action='store', nargs='+', required=True, metavar='Video(s)')

    args = parser.parse_args(argv[1:])
    script = import_module(args.script[0])
    script.main(args.videos)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os._exit(1)
    except Exception as e:
        dump()
        print(f'\nAn error has occured.\n> {e}')
        sys.exit(1)
