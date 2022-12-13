#!/usr/bin/env python3


import argparse
import sys
import os


def touch(file_path):
    '''Function touch() creates new file(s) in specified path
    Attention! This function raises FileExistsError if the file already exists
    
    Parameters:
    file_path (list): path list for new file(s)
    
    Returns: None
    '''
    
    for path in args.file_path:
        try:
            with open(path, 'x'): 
                os.utime(path, None)
        except FileExistsError:
            print(f'File exists: {path}! Try another name!')

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parser for touch function")
    parser.add_argument('file_path', help='path to files', nargs="+", default=sys.stdin)
    args = parser.parse_args()
    touch(args.file_path)

