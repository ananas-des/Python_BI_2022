#!/usr/bin/env python3


import argparse
import sys
import os


def ls_with_all(path_to_dir):
    '''Function ls_with_all() lists the content of the directory when --all flag is specified
    
    Parameters:
    path_to_dir (str): path to directory to be listed
    
    Returns: None
    (prints all directory content in std.out)
    '''
    
    # os.curdir and os.pardir for '.' and '..', respectively
    list_directory = sorted([os.curdir, os.pardir] + os.listdir(path_to_dir))
    sys.stdout.write('\n'.join(map(str, list_directory)) + '\n')
    
    
def ls_without_all(path_to_dir):
    '''Function ls_without_all() lists the content of the directory when --all flag is not specified
    
    Parameters:
    path_to_dir (str): path to directory to be listed
    
    Returns: None 
    (prints directory content without hidden files in std.out)
    '''
    
    list_directory = sorted([f for f in os.listdir(path_to_dir) if not f.startswith('.')])
    sys.stdout.write('\n'.join(map(str, list_directory)) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parser for ls command")
    parser.add_argument(
        'path_to_dir', help='path to directory', nargs='*', type=str, default=['.'], 
    )
    parser.add_argument(
        '-a', '--all', action='store_false',
        help='do not ignore entries starting with .'
    )
    args = parser.parse_args()
    
    # ls function choosing
    if not args.all: # --all not specified
        ls_func = ls_with_all
    else:
        ls_func = ls_without_all
    
    n_args = len(args.path_to_dir) # for making \n between output for multiple directories
    if n_args > 1:
        for n, path in enumerate(args.path_to_dir):
            sys.stdout.write(f'{path}:\n')
            ls_func(path)
            if n != (n_args - 1):
                sys.stdout.write('\n')
    else:
        ls_func(args.path_to_dir[0])          

