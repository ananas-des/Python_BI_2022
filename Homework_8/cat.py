#!/usr/bin/env python3


import argparse
import sys


def cat(path_to_file):
    '''Function cat() reads file and prints its content in std.output
    
    Parameters:
    path_to_file (str): path to file from input
    
    Returns: None
    (prints in std.output file content)
    '''
    
    with open(path_to_file) as file:
        text = file.read()
        sys.stdout.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parser for cat command")
    parser.add_argument(
        'file_path', nargs='+', default=sys.stdin, help='Input path to file(s)'
    )
    args = parser.parse_args()
    
    for path in args.file_path:
        cat(path)

