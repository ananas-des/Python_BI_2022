#!/usr/bin/env python3


import argparse
import os
import sys
import shutil


def rm(path_to_file, r_flag):
    '''Function rm() removes file(s) and empty directory(ies) and supportes recursive deletion
    of directory(ies) with content (if -r flag is specified in input)
    
    Parameters:
    path_to_file (str): path to file or directory to be removed
    
    Returns: None
    '''
    
    if os.path.isfile(path_to_file):
        os.remove(path_to_file)
    elif os.path.isdir(path_to_file):
        if not r_flag:
            shutil.rmtree(path_to_file)
        else:
            os.rmdir(path_to_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for rm function')
    parser.add_argument(
            'file_path', nargs='+', default=sys.stdin, help='Input path to file(s)'
        )
    parser.add_argument(
        '-r', '-R', '--recursive',
        action='store_false',
        help='Flag for removing directories and their contents recursively'
    )
    args = parser.parse_args() 
    for path in args.file_path:
        rm(path, args.recursive)          

