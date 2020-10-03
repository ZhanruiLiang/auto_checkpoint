import argparse
import sys
from . import auto_checkpoint

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('path', metavar='PATH', type=str, help='The path to watch')
    parser.add_argument('--interval', type=int, default=30, help='The refresh interval in seconds')
    args = parser.parse_args(argv)
    auto_checkpoint.watch(args.path, args.interval)

if __name__ == '__main__':
    main(sys.argv[1:])