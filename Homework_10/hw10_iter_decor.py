# Task1

class MyDict(dict):
    '''A derivative class of a regular dictionary, with the exception of iteration giving both keys and values'''
    
    
    def __iter__(self):
        self.iterator = iter(self.items())
        return self
    
    
    def __next__(self):
        return next(self.iterator)


# Task2

def iter_append(iterator, item):
    '''Apppends new element to the list iterator
    
    Parameters:
        iterator (list_iterator): list iterator
        item: any python object
    Yields: generator
    '''
    
    
    yield from iterator
    yield item
    
    
# Task3

def type_for_methods(cls):
    '''Searches for public class methods and sets type for their output
    
    Parametes:
        cls: class
    Returns: class with new type for class methods outputs
    '''
    
    
    for attr in dir(cls):
        if not attr.startswith('_') and callable(getattr(cls, attr)):
            setattr(cls, attr, change_type(getattr(cls, attr), cls))
    return cls


def change_type(func, cls):
    '''Function change_type() is a decorator for class and changes type of class method output 
    with MyString for strings and MySet for sets
    
    Parameters:
        func: class method
        cls: class
    Returns: inner_function
    '''
    
    
    def inner_function(*args, **kwargs):
        '''Determines the type of class method output and sets appropriate one
        
        Parameters:
            *args
            **kwargs
        Returns: result (MyString or MySet object)
        '''
        
        
        result = func(*args, **kwargs)
        if (cls == MyString and isinstance(result, str)) or ( # isinstance to strict str or set type output
            cls == MySet and isinstance(result, set)):
            return cls(result)
        else:
            return result
    return inner_function


@type_for_methods
class MyString(str):
    def reverse(self):
        return self.__class__(self[::-1])
    
    def make_uppercase(self):
        return "".join([chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char for char in self])
    
    def make_lowercase(self):
        return "".join([chr(ord(char) + 32) if 65 <= ord(char) <= 90 else char for char in self])
    
    def capitalize_words(self):
        return " ".join([word.capitalize() for word in self.split()])

    
@type_for_methods    
class MySet(set):
    def is_empty(self):
        return len(self) == 0
    
    def has_duplicates(self):
        return len(self) != len(set(self))
    
    def union_with(self, other):
        return self.union(other)
    
    def intersection_with(self, other):
        return self.intersection(other)
    
    def difference_with(self, other):
        return self.difference(other)
    

# Task4

def switch_privacy(cls):
    '''Switches privacy for class methods: 
    makes public methods to be private, and vice versa
    
    Parameters:
        cls: class
    Returns: class with switched public and private methods
    '''
    
    
    copy_attr_dict = cls.__dict__.copy()
    for attr in copy_attr_dict:
        if callable(getattr(cls, attr)):
            if not attr.startswith('_'):
                # private methods looks like "_ExampleClass__private_method" in dir
                setattr(cls, f'_{cls.__name__}__{attr}', getattr(cls, attr))
                delattr(cls, attr)
            elif attr.startswith(f'_{cls.__name__}__') and not attr.endswith('__'):
                setattr(cls, attr.split('__')[1], getattr(cls, attr))
                delattr(cls, attr)
    return cls


@switch_privacy
class ExampleClass:
    # Но не здесь
    def public_method(self):
        return 1
    
    def _protected_method(self):
        return 2
    
    def __private_method(self):
        return 3
    
    def __dunder_method__(self):
        pass
    
    
# Task5

import os
from dataclasses import dataclass


class OpenFasta:
    '''A class for reading .fasta files with biological sequences
    
    Record example: >Seq_ID Description(optional)
                    ATGTGGGAGGAAGGTGGGTGAAA
             
    Attributes:
        path (str): path to .fasta file
        
    Methods:
        read_record(): to read one record from .fasta file
        read_records(): to read multiple records from .fasta file
        
    Raises: ValueError if .fasta file does not exist in path        
    '''
    
    
    def __init__(self, path):
        '''Checks the existance of .fasta file and constructs all the necessary attributes

        Parameters:
            path (str): path to .fasta file
        
        Raises: ValueError if .fasta file does not exist in path
        '''
        
        
        if not os.path.isfile(path):
            file_path = path.split(os.path.sep)
            raise ValueError(f'No such {file_path[-1]}. Check path to file!')
    
        self.path = path
        
    
    def __enter__(self):
        self.f = open(self.path)
        return self
    
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        self.seq = []
        while True: 
            line = self.f.readline()
            if not line:
                if self.seq:
                    self.seq = ''.join(self.seq)
                    record = FastaRecord(id_=self.id_,
                                         description=self.description,
                                         seq=self.seq)
                    return record
                return ''
            elif line.startswith('>'):
                if self.seq:
                    self.seq = ''.join(self.seq)
                    record = FastaRecord(id_=self.id_,
                                         description=self.description,
                                         seq=self.seq)
                    self.id_, self.description = self.__handle_id_descr(line)
                    return record
                self.id_, self.description = self.__handle_id_descr(line)
            else:
                self.seq.append(line.strip())
                
                
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.f.close()
        pass
               
            
    def __handle_id_descr(self, line):
        '''Handles the first record line with Seq_ID and Description (optional)
        
        Parameters:
            line (str): record line
        Returns:
            id_ (str): record Seq_ID
            description (str): record description (if exists)
        '''
        
        
        vals = line.strip().split(' ', maxsplit=1)
        id_ = vals[0][1:]
        if len(vals) == 1:
            description = ''
        else: 
            description = vals[1]
        return id_, description
            
                
    def read_record(self):
        '''Reads fasta record
        
        Returns: FastaRecord
        '''
        
        
        return next(self)
    
    
    def read_records(self):
        '''Reads all fasta records in file and appends them to list
        
        Returns: records (list)
        '''
        
        
        records = []
        record = self.read_record()
        while record:
            records.append(record)
            record = self.read_record()
        return records
              

@dataclass
class FastaRecord:
    '''A dataclass with information about fasta record
    
    Parameters:
        id_ (str): record id (Seq_ID)
        description (str): record description (if exists)
        seq (str): biological sequences
    '''
    
    
    id_: str
    description: str
    seq: str
    
    
# Example1. Reading one fasta record from file
with OpenFasta(os.path.join("data", "example.fasta")) as fasta:
    record = fasta.read_record()
    print(f'FastaRecord form file:\n{record}')
    print(f'Seq_ID: {record.id_}\nSeq: {record.seq}')
    print(type(record))
    
# Example2. Reading all fasta records from file
with OpenFasta(os.path.join("data", "example.fasta")) as fasta:
    print(f'All FastaRecords from file:')
    for record in fasta.read_records():
        print(record)
        
# Example3. At the end of the file acts like `readlines()`
with OpenFasta(os.path.join("data", "example.fasta")) as fasta:
    for _ in range(10):
        print(fasta.read_record())
        

# Task6