# Repository for Python Homeworks in IB
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

We have acquired many basic and advanced programming skills in the Python course at **Bioinformatics Institute**. During the course, we have learned how to work with lots of Python labraries, such as:

- `sys`, `os`;
- `numpy`, `pandas`;
- `matplotlib`, `seaborn`;
- `re`, `io`, `argparse`;
- `dataclasses`, `functools`;
- `concurrent`, `multiprocessing`, `threading`;
- `requests`, `bs4`, `python-dotenv`, *etc.*

Here are brief descriptions of the tasks that we performed to master the topics. Folders contains tasks solutions, their descriptions, and required system and Python packages.

## Homework12. [Parallel programming](hw12_parallel_prog) 🚥

[Here](hw12_parallel_prog) some solutions for Python **Parallel Programming** Tasks using `sklearn`, `numpy`, and some built-in packages for parallel programming in Python, such as `concurrent`, `multiprocessing`, and `threading`. During the tasks, we parallelized `fit()`, `predict_proba()`, and `predict()` methods for custom implementation of *Random Forest Classifier*, created decorator function `memory_usage()` to limit the memory usage of a target function and a class `ParallelMap` that parallelizes the map function using multiprocessing.

## Homework10. [Decorators and iterators](hw10_iter_decor) :performing_arts: :loop:

[Here](hw10_iter_decor) some solutions for Python **decorators and iterators** Tasks using `os`, `dataclasses`, and `functools` modules. During the tasks, we create *a derivative class of a regular dictionary*, with the exception of iteration giving both keys and values, function that appends new element to the list iterator returning iterator, decorator for class methods to return current class objects, context manager for reading `.fasta` files and storing them in dataclass `FastaRecord()` format, replaced all public methods to private, and *vice versa*, using decorator `switch_privacy()`, and wrote a script for finding all possible (non-unique) genotypes when crossbreeding two organisms and calculated the probability of a certain genotype (its expected share in the offspring.

## Homework7. [Functional programming](hw7_func_programming) 🔀

Utility [functional.py](hw7_func_programming/functional.py) provides some functions for functional programming tasks, such as *sequential_map*, *consensus_filter*, 
*conditional_reduce*, *func_chain*, *multiple_partial*, and *nothing_to_print*. This functions based on bare Python source and built-in `sys` package.

## Homework6. [Regular expressions](hw6_regexp) :paperclip:

[Here](hw6_regexp) some solutions for Python **regular expressions** Tasks using `re` module. During the tasks, we parsed FTP links, analized *2430 A.D. short story by Isaac Asimov* text, wrote script for translator from Russian to "brick language", *etc.*

## Homework5. [Pandas and plots](hw5_pandas_and_plots) 📈

[Here](hw5_pandas_and_plots) some solutions for Python `pandas` and plot customization Tasks using `matplotlib` and `seaborn`. During the task, we created function for reading `.gff` and `.bed` files and converting them into `pandas.DataFrame`, reconstructed `bedtools intersect` using `pandas`, created and customized **volcano plot** based on differential expression data, created and customized **bar of pie chart** where the first slice of the pie is "exploded" into a bar chart with a further breakdown of certain slice's characteristics.

## Homework4. [Numpy](hw4_numpy) 🔢 @ 🔡

Utility [numpy_challenge.py](hw4_numpy/numpy_challenge.py) provides some functions for dealing with *one and two dimensional matrices* given in `numpy.array` format, 
such as *matrix multiplication*, *multidimensional distance computation*, and *distance matrix generation*. This functions based on Python **NumPy package**. 
You may use [numpy_challenge.py](hw4_numpy/numpy_challenge.py) functions in other programm after importing the utility as module `import numpy_challenge as {name}`. 
If you run [numpy_challenge.py](hw4_numpy/numpy_challenge.py) as the main program, it will also generate **three different numpy.arrays** and put them into `std.output`. 

## Homework3. [Virtual environments](hw3_venv) 🔧

Programmer Mikhail published comprehensive study focused on **python modules** and **virtual environments**. In *Supplementary* he attached a link 
to the repository on *Github* with [his code](https://github.com/krglkvrmn/Virtual_environment_research). Unfortunately, the utility [ultraviolence.py](hw3_venv/ultraviolence.py) was not adapted for widespread usage. Here some guidlines with [requirements.txt](hw3_venv/requirements.txt) for proper launch of Mikhail's script on **Ubuntu 22.04.1 LTS** with **Python v3.11.0a7**. 

## Homework2. [FastQ filtrator](hw2_fastq_filtrator) 🛂

Utility [fastq_filtrator.py](hw2_fastq_filtrator/fastq_filtrator.py) deals with `.fastq` files. It opens *input `.fastq` file*, calculates *Q-score*, *GC-content*, and *length* 
for every read in file. According to calculated read *Q-score*, *GC-content*, and *length*, it performs **three types of read filtering** using values of ```_bound``` variables. As the result, [fastq_filtrator.py](hw2_fastq_filtrator/fastq_filtrator.py) creates *_passed.fastq* file with passed reads using your ```output_file_prefix```. If you pass to ```save_filtered``` variable boolean ```True```, it also allows to generate *_failed.fastq* file with failed reads. This utility is conveniet for *multiple filtering* of the same *input `.fastq` file*.

## Homework1. [Collections](hw1_collections) 🐳

Utility [hw1_Collections.py](hw1_collections/hw1_Collections.py) provides some basic tools for working with *nucleic acid sequences*. Based on python dictionaries and the complementarity principle, 
this script allows to make complement sequences for DNA and RNA, to reverse them, and to transcribe RNA sequence from DNA template. 
For your convenience [hw1_Collections.py](hw1_collections/hw1_Collections.py) is not case-sensitive, and all charachters in output sequences in accordance with input register.
