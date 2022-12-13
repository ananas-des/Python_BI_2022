#!/usr/bin/env python3


import argparse
import sys
import shutil


def mv(file_path, move_to_path):
    '''Function mv() moves or renames file(s)/directory(ies) from one path to another
    
    Parameters:
    file_path (list): list with file(s)/directory(ies) for moving
    move_to_path (str): specified destination for file(s)/directory(ies)
    
    Returns: None
    '''
    for from_path in args.file_path:
        shutil.move(from_path, move_to_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parser for move function")
    parser.add_argument('file_path', help="file(s)/directory(ies) path for moving", nargs='+', default=sys.stdin)
    parser.add_argument('move_to_path', help="destination for file(s)/directory(ies)", type=str, default=sys.stdin)
    args = parser.parse_args()
    mv(args.file_path, args.move_to_path)

