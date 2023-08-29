# Decorators and Iterators :performing_arts: :loop:

# Homework10

Here some solutions for Python **decorators and iterators** Tasks using `os`, `dataclasses`, and `functools` modules.

### System
This code was tested on **Ubuntu 22.04.1 LTS** with **Python version 3.9.13**.

*Note: only standard Python packages used in this code.*

### Files
In this directory there are *three files*: [README.md](./README.md), [hw10_iter_decor.ipynb](./hw10_iter_decor.ipynb), and [hw10_iter_decor.py](./hw10_iter_decor.py).

- **README.md**: discriptions for files in this directory 
- **hw10_iter_decor.ipynb**: jupyter notebook with Tasks solutions
- **hw10_iter_decor.py**: .py file with only code from jupyter notebook

### Folders

In [data](./data) folder there is [example.fasta](./data/example.fasta) .fasta file for testing **Task5** context manager `OpenFasta()`.

## Task1. Class MyDict

- create a derivative class of a regular dictionary, with the exception of iteration giving both keys and values

## Task2. Yield, or not to Yield

- create function that appends new element to the list iterator returning iterator

## Task3. Classes MyString an MySet

- create decorator for class methods to return current class objects 

## Task4. Form public to private, and vice versa

- replace all public methods to private, and vice versa, using decorator `switch_privacy()`

## Task5. Context manager OpenFasta

- create context manager for reading .fasta files and storing them in dataclass `FastaRecord()` format

## Task6. Crossbreed them all!

- get all possible (non-unique) genotypes when crossbreeding two organisms and calculate the probability of a certain genotype (its expected share in the offspring)
