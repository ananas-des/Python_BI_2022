#!/usr/bin/env python3


import argparse
import sys


def sort(words):
    '''Function sort() sorts words in given file(s) in decreasing lexicographic order
    Attention! As original bash sort, this function splits file(s) content by '\n'
    and takes full line as single "word" 
    
    Parameters:
    words (set): words set from given file(s)
    
    Returns: None
    (writes in std.out sorted file(s) content)    
    '''
    
    sorted_words = sorted(words)
    sys.stdout.write('\n'.join(map(str, sorted_words)) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parser for sort function')
    words_list = list() # for keeping words from file(s)
    parser.add_argument(
        'file_path', nargs='*', default=sys.stdin, help='Input path to file(s)'
    )
    args = parser.parse_args()

    for path in args.file_path:
        with open(path, 'r') as file:
            text = list(file.read().strip().split('\n')) # reading file and putting its words in list
        words_list += text    
    sort(words_list)
