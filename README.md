# Repository for Python Homeworks in IB

## Homework12

Here some solutions for Python **Parallel Programming** Tasks using `sklearn`, `numpy`, and some built-in packages for parallel programming in Python, such as `concurrent`, `multiprocessing`, and `threading`.

### Task1. Paralleling custom Random Forest

- parallelize `fit()`, `predict_proba()`, and `predict()` methods for custom implementation of Random Forest Classifier

### Task2. Memory usage decorator

- decorator function `memory_usage()` to limit the memory usage of a target function

### Task3. Custom Parallel mapping

- a class `ParallelMap` that parallelizes the map function using multiprocessing

## Homework10

Here some solutions for Python **decorators and iterators** Tasks using `os`, `dataclasses`, and `functools` modules.

### Task1. Class MyDict

- create a derivative class of a regular dictionary, with the exception of iteration giving both keys and values

### Task2. Yield, or not to Yield

- create function that appends new element to the list iterator returning iterator

### Task3. Classes MyString an MySet

- create decorator for class methods to return current class objects 

### Task4. Form public to private, and vice versa

- replace all public methods to private, and vice versa, using decorator `switch_privacy()`

### Task5. Context manager OpenFasta

- create context manager for reading .fasta files and storing them in dataclass `FastaRecord()` format

### Task6. Crossbreed them all!

- get all possible (non-unique) genotypes when crossbreeding two organisms and calculate the probability of a certain genotype (its expected share in the offspring)

## Homework7

Utility [functional.py](hw7_func_programming/functional.py) provides some functions for functional programming tasks, such as *sequential_map*, *consensus_filter*, 
*conditional_reduce*, *func_chain*, *multiple_partial*, and *nothing_to_print*. This functions based on bare Python source and built-in `sys` package.

## Homework6

Here some solutions for Python **regular expressions** Tasks using `re` module. 

### Task1. FTP links parsing

- create *ftps* file with all **ftp links** from **references** file

### Tasks2-5. Regular expressions for 2430 A.D. short story by Isaac Asimov

- search all numbers in story;
- search all words with 'A' or 'a' letters;
- parse all exclamation sentences;
- plot the distribution of the unique words lengths;

### Task6. From Russian to Brickish

- create translator from Russian to "brick language"

### Task7. Sentences with a given number of words

- make function to find n-words sentences and return a list of tuples with words from the resulted sentences

All required data files are [here](hw6_regexp/data).

## Homework5

Here some solutions for Python `pandas` and plot customization Tasks using `matplotlib` and `seaborn`. 

### Task1. Real Data

- create functions for reading `.gff` and `.bed` files and converting them into `pandas.DataFrame`;
- make **rRNA_barplot** with rRNA type counts for each reference genome based on [rrna_annotation.gff](hw5_pandas_and_plots/data/rrna_annotation.gff) data;
- reconstruct `bedtools intersect` using `pandas`

### Task2. Plot customization

- read [diffexpr_data.tsv.gz](hw5_pandas_and_plots/data/diffexpr_data.tsv.gz) file;
- create and customize **volcano plot** based on differential expression data from given file

### Task3. Pie Chart

- create and customize **bar of pie chart** where the first slice of the pie is "exploded" into a bar chart with a further breakdown of said slice's characteristics on [Top_100_Languages.csv](hw5_pandas_and_plots/data/Top_100_Languages.csv) (arbitrary data)

All mentioned data files are [here](hw5_pandas_and_plots/data).

## Homework4

Utility [numpy_challenge.py](hw4_numpy/numpy_challenge.py) provides some functions for dealing with *one and two dimensional matrices* given in `numpy.array` format, 
such as *matrix multiplication*, *multidimensional distance computation*, and *distance matrix generation*. This functions based on Python **NumPy package**. 
You may use [numpy_challenge.py](hw4_numpy/numpy_challenge.py) functions in other programm after importing the utility as module `import numpy_challenge as {name}`. 
If you run [numpy_challenge.py](hw4_numpy/numpy_challenge.py) as the main program, it will also generate **three different numpy.arrays** and put them into `std.output`. 

## Homework3

Programmer Mikhail published comprehensive study focused on **python modules** and **virtual environments**. In *Supplementary* he attached a link 
to the repository on *Github* with [his code](https://github.com/krglkvrmn/Virtual_environment_research). Unfortunately, the utility [ultraviolence.py](hw3_venv/ultraviolence.py) was not adapted for widespread usage. Here some guidlines with [requirements.txt](hw3_venv/requirements.txt) for proper launch of Mikhail's script on **Ubuntu 22.04.1 LTS** with **Python v3.11.0a7**. 

## Homework2

Utility [fastq_filtrator.py](hw2_fastq_filtrator/fastq_filtrator.py) deals with `.fastq` files. It opens *input `.fastq` file*, calculates *Q-score*, *GC-content*, and *length* 
for every read in file. According to calculated read *Q-score*, *GC-content*, and *length*, it performs **three types of read filtering** using values of ```_bound``` variables. As the result, [fastq_filtrator.py](hw2_fastq_filtrator/fastq_filtrator.py) creates *_passed.fastq* file with passed reads using your ```output_file_prefix```. If you pass to ```save_filtered``` variable boolean ```True```, it also allows to generate *_failed.fastq* file with failed reads. This utility is conveniet for *multiple filtering* of the same *input `.fastq` file*.

## Homework1

Utility [hw1_Collections.py](hw1_collections/hw1_Collections.py) provides some basic tools for working with *nucleic acid sequences*. Based on python dictionaries and the complementarity principle, 
this script allows to make complement sequences for DNA and RNA, to reverse them, and to transcribe RNA sequence from DNA template. 
For your convenience [hw1_Collections.py](hw1_collections/hw1_Collections.py) is not case-sensitive, and all charachters in output sequences in accordance with input register.
