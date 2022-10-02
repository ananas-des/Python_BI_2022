#!/usr/bin/env python
# coding: utf-8

# In[249]:


def sequence_check (nucleic_acid):
    '''This function tests whether sequence from input is DNA, RNA or not a nucleic acid
    
    Parameters:
    nucleic_acid list(): literal sequence from the input with any characters
    
    Returns:
    "DNA" (str): "Sequence is DNA" (if input contains only A, T, G, or C deoxynucleotides)
    "RNA" (str): "Sequence is RNA" (if input contains only A, U, G, or C ribonucleotides)
    "Not nucleic acid": "Not nucleic acid" (for any other sequences)
    '''
    
    sequence_is_DNA = True
    sequence_is_RNA = True
        
    for i in nucleic_acid:
        if i not in complement_DNA_dictionary.keys(): #Keys in this dictionary DNA nucleotides
            sequence_is_DNA = False
        if i not in transcription_dictionary.values(): #Values in this dictionary RNA nucleotides
            sequence_is_RNA = False
        
    if (len(nucleic_acid) == 0) | (sequence_is_DNA | sequence_is_RNA == False): 
    #Here sequence type would be checked and returned
        return "Not nucleic acid"
    elif sequence_is_DNA == True:
        return "DNA"
    elif sequence_is_RNA:
        return "RNA"
                    

def complement(nucleic_acid, sequence_type):
    '''This function transforms DNA or RNA sequence into its complement
    
    Parameters:
    nucleic_acid (list): DNA or RNA sequence from the input()
    sequence_type (str): type of nucleic acid
    
    Returns:
    complement_nucleic_acid (str): complemented DNA or RNA sequence
    '''
    
    complement_nucleic_acid = "" #Empty str is initiated   
    if sequence_type == "DNA":
        for i in nucleic_acid:
            complement_nucleic_acid += complement_DNA_dictionary[i] #complement_DNA_dictionary contains DNA nucleotides
        return complement_nucleic_acid
    if sequence_type == "RNA":
        for i in nucleic_acid:
            complement_nucleic_acid += complement_RNA_dictionary[i] #complement_RNA_dictionary contains RNA nucleotides
        return complement_nucleic_acid

    
def reverse_complement(nucleic_acid, sequence_type):
    '''This function reverse DNA or RNA sequence and makes its complement using 
    reverse() and complement() functions
    
    Parameters:
    nucleic_acid (list): DNA or RNA sequence from the input()
    sequence_type (str): type of nucleic acid
    
    Returns:
    complement_nucleic_acid (str): reversed and complemented DNA or RNA sequence
    '''
    
    complement_nucleic_acid = reverse(complement(nucleic_acid, sequence_type))
    return complement_nucleic_acid
            

def transcription(nucleic_acid):
    '''This function transcribes DNA sequence from the input
    Attention! Only DNA sequence would be transcribed!
    
    Parameters:
    nucleic_acid (list): DNA sequence from the input()
    
    Returns:
    transcript (str): transcribed input sequence (RNA from DNA template)
    '''

    transcript = "" #Empty str is initiated
    for i in nucleic_acid:
        transcript += transcription_dictionary[i] #keys are DNA nucleotides, and values are RNA nucleotides
    return transcript


def reverse(nucleic_acid):
    '''This function reverses DNA or RNA sequence
    
    Parameters:
    nucleic_acid (list): DNA or RNA sequence from the input()
    
    Returns:
    reversed_nucleic_acid (str): reversed DNA or RNA from the input
    '''
    reversed_nucleic_acid = ''.join(nucleic_acid[::-1]) #Reverses nucleic_acid and changes type to str()
    return reversed_nucleic_acid

complement_DNA_dictionary = {'A': 'T', 'a': 't', 'T': 'A', 't': 'a',
                            'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g'} #Dictionary for DNA complement()
complement_RNA_dictionary = {'A': 'U', 'a': 'u', 'U': 'A', 'u': 'a', 
                            'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g'} #Dictionary for RNA complement()
transcription_dictionary = {'A': 'A', 'a': 'a', 'T': 'U', 't': 'u',  
                           'G': 'G', 'g': 'g', 'C': 'C', 'c': 'c'} #Dictionary for transcription()

while True: 
    #Face-control for command input
    command = input("Enter command: ")
    if (command == "exit") | (len(command) == 0): #If for command input is "exit" or nothing, program will interupt
        print("See you soon:)")
        break
    #Face-control for nucleic_acid input    
    while True:
        nucleic_acid = list(input("Enter sequence: "))            
        sequence_type = sequence_check(nucleic_acid) #Calling function sequence_check()
        if sequence_type == "Not nucleic acid":
            print("Invalid alphabet: Type another sequence!") #Input should be only DNA or RNA
        else:
            break
    
    #Realization of Commands      
    if command == 'complement':
        result = complement(nucleic_acid,sequence_type)
        print(f'Your complemented {sequence_type} sequence: {result}')
    elif (command == 'transcribe') & (sequence_type == 'DNA'):
        result = transcription(nucleic_acid)
        print(f'Your transcribed DNA sequence: {result}')
    elif command == 'reverse':
        result = reverse(nucleic_acid)
        print(f'Your reversed {sequence_type} sequence: {result}')
    elif command == 'reverse_complement':
        result = reverse_complement(nucleic_acid, sequence_type)
        print(f'Your reversed complement {sequence_type} sequence: {result}')
    else:
        print(f'Wrong command: {command} for {sequence_type}') #In case of undefined commands or wrong types

