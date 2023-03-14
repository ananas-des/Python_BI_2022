import os
from dataclasses import dataclass
from functools import lru_cache
from datetime import datetime


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

from functools import lru_cache
from datetime import datetime


# Ваш код здесь (1 и 2 подзадание)
def calc_runtime(func):
    '''Decorator for calculatinf function runtime'''
    
    
    def inner_function(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        stop = datetime.now()
        print(stop - start)
        return result
    return inner_function  


def parse_genotype(genotype):
    '''Parses genotypes to obtain alleles
    
    Parameters:
        genotype (str): genotype, example: 'Aabb'
    
    Returns: list of alleles
    '''
    
    
    return [genotype[i:i+2] for i in range(0, len(genotype), 2)]


def calc_gamets(*args):
    '''Creates sets with all possible gamets for genotype
    
    Parameters:
        *args (alleles returned by parse_genotype())
    Returns: generator with all possible gamets for genotype
    '''
    
    
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
        

@lru_cache(maxsize=None)
def do_genotype(*gamets):
    '''Makes genotype from gamets
    
    Parameters:
        gamets (tuples): two sets of gamets
    Returns: 
        genotype (str): resulted genotype
    '''
    
    
    genotype = ''.join([''.join(sorted(gene)) for gene in zip(*gamets)])
    return genotype

        
def calc_genotypes(gamets1, gamets2, k=1):
    '''Creates all possible genotypes from two sets of gamets
    
    Parameters:
        gamets1 (tuple): set of gamets for the first genotype
        gamets2 (tuple): set of gamets for the second genotype
        k (int): number of genes devided by two
    
    Returns: generator with possible genotypes
    '''
    
    
    for gamet1 in gamets1:
        for gamet2 in gamets2:
            geno_l = do_genotype(gamet1[:k], gamet2[:k])
            geno_r = do_genotype(gamet1[k:], gamet2[k:])
            yield geno_l + geno_r   

            
def all_genotypes(p1, p2):
    '''Creates all possible offspring genotypes for given parental genotypes
    
    Parameters:
        p1 (str): parent1 genotype
        p2 (str): parent2 genotype
        
    Returns: None
    '''
    
    
    gamets1 = tuple(calc_gamets(*parse_genotype(p1)))
    gamets2 = tuple(calc_gamets(*parse_genotype(p2)))
    [print(genotype) for genotype in calc_genotypes(gamets1, gamets2)]
    

@calc_runtime
def genotype_prob(p1, p2, target):
    '''Calculates the probability of a certain genotype (its expected share in the offspring)
    
    Parameters:
        p1 (str): parent1 genotype
        p2 (str): parent2 genotype
        target (str): target offspring genotype for its probability calculation
        
    Returns: float (probability)
    '''
    
    
    gamets1 = tuple(calc_gamets(*parse_genotype(p1)))
    gamets2 = tuple(calc_gamets(*parse_genotype(p2)))
    
    total_count = target_count = 0
    k = len(p1) // 4
    genotypes = calc_genotypes(gamets1, gamets2, k)
    for genotype in genotypes:
        total_count += 1
        if target == genotype:
            target_count +=1
    return target_count/total_count


# example for Subtask1
parent1 = 'Aabb'
parent2 = 'Aabb'
all_genotypes(parent1, parent2)

# example for Subtask2
parent1 = 'Aabb'
parent2 = 'Aabb'
target = 'Aabb'
genotype_prob(parent1, parent2, target)

# Ваш код здесь (3 подзадание)
@calc_runtime
def unique_with(p1, p2, target):
    '''Finds all unique genotypes with certain alleles combination
    
    Parameters:
        p1 (str): parent1 genotype
        p2 (str): parent2 genotype
        target (str): target offspring genotype
        
    Returns: None
    '''
    
    
    gamets1 = tuple(calc_gamets(*parse_genotype(p1)))
    gamets2 = tuple(calc_gamets(*parse_genotype(p2)))
    
    unique = []
    for genotype in calc_genotypes(gamets1, gamets2):
        if (genotype.find(target) != -1) and (genotype not in unique):
            unique += [genotype]
            print(genotype)
            
            
# example for Subtask3
parent1 = 'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'
parent2 = 'АаббВвГгДДЕеЖжЗзИиЙйКкЛлМмНН'
target = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛл'
unique_with(parent1, parent2, target)

# Ваш код здесь (4 подзадание)
# example for Subtask4
parent1 = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн'
parent2 = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНн'
target = 'АаБбввГгДдЕеЖжЗзИиЙйккЛлМмНн'
genotype_prob(parent1, parent2, target)