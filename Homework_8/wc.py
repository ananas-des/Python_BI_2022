#!/usr/bin/env python3


import argparse
import sys


def wc_l(file):
    '''Function wc_l() counts number of lines in file
    Attention! This function counts number of '\n' in file as bash wc, so misses the last line if ends without \n
    
    Parameters:
    file (list): list with file content
    
    Returns:
    n_lines (int): number of lines
    '''
    
    n_lines = len(file)
    return n_lines


def wc_w(file):
    '''Function wc_w() counts number of words in file
    
    Parameters:
    file (list): list with file content
    
    Returns:
    n_words (int): number of words
    '''
    
    n_words = [item for sublist in file for item in sublist.split()]
    return len(n_words)
    

def wc_c(file):
    '''Function wc_c() counts number of characters in file
    
    Parameters:
    file (list): list with file content
    
    Returns:
    n_bytes (int): number of characters
    '''
    
    n_bytes = len([item for sublist in file for item in sublist]) + wc_l(file)
    return n_bytes

    
def args_dict(args): # dictionary for input parameters
    '''Function args_dict() creates dictionary with keys and values from argparse.Namespace object
    for optional parameters (-l, -w, and -c) and counts their number
    
    Parameters:
    args (argparse.Namespace): object with parameters for .py script
    
    Returns:
    func_dictionary (dict): dictionary with optional parameters and their values (bool)
    n_col (int): number of specified parameters for .py script    
    '''
    
    func_dictionary = {
        wc_l: args.lines,
        wc_w: args.words,
        wc_c: args.bytes,
    }
    if all(func_dictionary.values()):
        n_col = 3
    else:
        n_col = 3 - sum(func_dictionary.values())
    return func_dictionary, n_col


def proc_txt(func_dictionary, text):
    '''Function proc_txt() processes given file according to specified input parametes
    
    Parameters:
    func_dictionary (dict): dictionary with optional parameters and their values (bool)
    text (str): file from input
    
    Returns:
    output (list): list with funtions results for std.output
    '''
    
    output = []
    if all(func_dictionary.values()):
        for func in func_dictionary.keys():
            output.append(func(text))
    else:
         for func, value in func_dictionary.items():
                if not value:
                    output.append(func(text))
    
    return output
            
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for wc function')
    parser.add_argument(
        '-l', '--lines',
        action='store_false',
        help='Flag for counting lines in file(s)'
    )
    parser.add_argument(
        '-w', '--words',
        action='store_false',
        help='Flag for counting words in file(s)'
    )
    parser.add_argument(
        '-c', '--bytes',
        action='store_false',
        help='Flag for counting characters in file(s)'
    )
    parser.add_argument(
        'file_path', nargs='*', help='Input path to file(s)'
    )
    args = parser.parse_args()
    
    func_dict, n_col = args_dict(args)
    total = [0] * n_col # for final total output as in bash wc
    
    if len(args.file_path) == 0 or args.file_path[0] == "-":
        text = [i.strip() for i in sys.stdin]
        output = proc_txt(func_dict, text)
        sys.stdout.write(' ' + '  '.join(map(str, output)) + '\n')
    else:    
        for fp in args.file_path:
            output = []
            with open(fp, 'r', encoding='UTF-8') as file:
                text = file.read().strip().split("\n")
            output = proc_txt(func_dict, text)
            total = [total[i] + output[i] for i in range(n_col)]
            output.append(f'{fp}\n')
            sys.stdout.write(' ' + '  '.join(map(str, output)))
        if len(args.file_path) > 1:
            total.append('total\n')
            sys.stdout.write(' '.join(map(str, total)))
