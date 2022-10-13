#!/usr/bin/env python
# coding: utf-8

# In[15]:


import os # for using os.path.isfile() and os.remove() functions

def main(input_fastq, output_file_prefix, save_filtered = False, 
         gc_bounds = (0,100), length_bounds = (0, 2**32), quality_threshold = 0):
    '''Function main() deals with .fastq files. It opens .fastq, can calculates Q-score, GC-content, and length 
    for every read in file. According to values of _bound variables for each test, it filters reads and creates 
    '_passed.fastq' file with passed reads. If you also need '_failed.fastq' file with failed reads, you need to
    pass to 'save_filtered' boolean True.
    
    Parameters:
    input_fastq (str): path to .fastq file
    output_file_prefix (str): first part of the output file(s) name(s)
    save_filtered (bool): variable for decision about failed reads (True for saving them into '_failed.fastq' 
        file or not). Default is boolean False
    gc_bounds (int, float, tuple, list): threshold(s) for read GC-content test. Default is (0, 100), single 
        int or float in gc_bounds is accepted as max boundary.
    length_bounds (int, tuple, list): threshold(s) for read length test. Default is (0, 2**32), single int
        in length_bounds is accepted as max boundary.
        Attention! length_bounds can't be float!
    quality_threshold (int): threshold for read quality test. Default is 0
    
    Returns: None
    '''  
    # removing output files with prefix if they are pre-existed
    # for multimple function usage on the same input .fastq  
    if os.path.isfile(output_file_prefix + '_passed.fastq'):
        os.remove(output_file_prefix + '_passed.fastq')
    if os.path.isfile(output_file_prefix + '_failed.fastq'):
        os.remove(output_file_prefix + '_failed.fastq')
    
    with open(input_fastq) as row_data:
        while True:
            seq_read = get_read(row_data)
            if seq_read[0] == '':
                break
            name, sequence, description, ascii_code = seq_read # naming of seq_read (list) elements
            q_test = qscore_filter(ascii_code, quality_threshold) # variable for qscore_filter() return
            gc_test = gc_content_filter(sequence, gc_bounds) # variable for gc_content_filter() return
            length_test = length_filter(sequence, length_bounds) # variable for length_filter() return
            output_generator(seq_read, q_test, gc_test, length_test, # calling function for output .fastq generation
                             output_file_prefix, save_filtered)

def get_read(row_data):
    '''This function gets one read (four strings) from input .fastq file and transforms it into list.
    
    Parameters:
    row_data (opened input .fastq file): variable generated during input_fastq file opening
    
    Returns:
    seq_read (list): all information about one read
    '''
    
    # getting list of read information (4 strings)
    seq_read = [row_data.readline().strip() for _ in range(4)]
    return seq_read


def qscore_filter(ascii_code, quality_threshold):
    '''This function calculates Q-score for every read in input .fastq file. 
    It decodes each nucleotide quality given in ASCII format into numeric Phred33 format and determines mean 
    value for read. After calculations function checks, whether read quality meets quality threshold. 
    
    Parameters:
    ascii_code (list): characters in ASCII format given in 4th string for every read
    quality_threshold (int): threshold for read quality test (equals to 0 by default)
    
    Returns: bools after read quality checkout 
    True - if read passed checkout (read quality >= quality_threshold)
    '''
    
    all_q_scores = 0
    # cycle for nucleotide quality decoding in Phred33
    for character in ascii_code:
        q_score = ord(character) - 33
        all_q_scores += q_score
    read_quality = all_q_scores / len(ascii_code) # mean read quality calculation
    
    # mean read quality test using variable quality_threshold
    return read_quality >= quality_threshold

    
def gc_content_filter(sequence, gc_bounds):
    '''This function calculates percentage of GC nucleotides for every read in input .fastq file.
    After calculations function checks, whether GC-content meets gc_bounds.  
    
    Parameters:
    sequence (str): nucleic acid sequence given in 2nd string for every read
    gc_bounds (int, float, tuple, list): threshold(s) for read GC-content test (equals to (0, 100) by default), single 
        int or float in gc_bounds is accepted as max boundary. 
    
    Returns: bools after read GC-content checkout
    True - if read passed checkout (read GC-percentage lies in gc_bounds)  
    '''
    # type determination of gc_bounds variable
    # and setting up GC-content test thresholds
    if type(gc_bounds) in (int, float):
        min_gc = 0
        max_gc = gc_bounds
    else:
        min_gc, max_gc = gc_bounds
    
    g_number = sequence.count('G') # counting G in read
    c_number = sequence.count('C') # counting C in read
    gc_content = (g_number + c_number) / len(sequence) * 100 # GC-content calculation
    
    # read GC-content test using thresholds based on gc_bounds variable
    return min_gc <= gc_content <= max_gc 

    
def length_filter(sequence, length_bounds):
    '''This function calculates length for every read in input .fastq file.
    After calculations function checks, whether read length meets length_bounds.
    
    Parameters:
    sequence (str): nucleic acid sequence given in 2nd string for every read
    length_bounds (int, tuple, list): threshold(s) for read length test (equals to (0, 2**32) by default), single int
        in length_bounds is accepted as max boundary.
    Attention! length_bounds can't be float!
    
    Returns: bools after read length checkout
    True - if read passed checkout (read length lies in length_bound)  
    '''
    
    # type determination of length_bounds variable
    # and setting up length test thresholds 
    if type(length_bounds) is int:
        min_length = 0
        max_length = length_bounds
    else:
        min_length, max_length = length_bounds
    
    # read length test using thresholds based on length_bounds variable
    return min_length <= len(sequence) <= max_length

    
def output_generator(seq_read, q_test, gc_test, length_test, 
                     output_file_prefix, save_filtered):
    '''Function output_generator() generates one or two files with reads from input .fastq file after their 
    filtering. It creates you '_passed.fastq' with passed reads. If you choosed "True" for save_filtered 
    variable, it will also generates '_failed.fastq' file with failed reads.
        
    Parameters:
    seq_read (list): all information about one read
    q_test (bool): qscore_filter function return (True for passed read)
    gc_test (bool): gc_content_filter function return (True for passed read)
    length_test (bool): length_filter function return (True for passed read)
    output_file_prefix (str): first part of the output file(s) name(s)
    save_filtered (bool): variable for decision about failed reads (True for saving them into '_failed.fastq' 
        file or not)
    
    Returns: None
    '''
    
    # appending reads into output .fastq
    if False in (q_test, gc_test, length_test):
        # appending reads into _failed.fastq file, variable save_filtered = True
        if save_filtered:
            with open(output_file_prefix+'_failed.fastq', 'a') as failed_reads:
                for read_str in seq_read:
                    failed_reads.write(read_str+'\n')
    else:
        with open(output_file_prefix+'_passed.fastq', 'a') as passed_reads:
                for read_str in seq_read:
                    passed_reads.write(read_str+'\n')

