# Repository for Python Homeworks in IB

## Homework4

Utility **numpy_challenge.py** provides some functions for dealing with *one and two dimensional matrices* given in `numpy.array` format, 
such as *matrix multiplication*, *multidimensional distance computation*, and *distance matrix generation*. This functions based on Python **NumPy package**. 
You may use **numpy_challenge.py** functions in other programm after importing the utility as module `import numpy_challenge as {name}`. 
If you run **numpy_challenge.py** as the main program, it will also generate **three different numpy.arrays** and put them into `std.output`. 
Here some guidelines for how to use this script and how does it work.

## Homework3

Programmer Mikhail published comprehensive study focused on **python modules** and **virtual environments**. In *Supplementary* he attached a link 
to the repository on *Github* with [his code](https://github.com/krglkvrmn/Virtual_environment_research). Unfortunately, the utility **ultraviolence.py** was not adapted 
for widespread usage. Here some guidlines with **requirements.txt** for proper launch of Mikhail's script on **Ubuntu 22.04.1 LTS** with **Python v3.11.0a7**. 

## Homework2

Utility **fastq_filtrator.py** deals with **.fastq files**. It opens *input .fastq file*, calculates *Q-score*, *GC-content*, and *length* 
for every read in file. According to calculated read *Q-score*, *GC-content*, and *length*, it performs **three types of read filtering** using values of ```_bound``` variables. As the result, **fastq_filtrator.py** creates *_passed.fastq* file with passed reads using your ```output_file_prefix```. If you pass to ```save_filtered``` variable boolean ```True```, it also allows to generate *_failed.fastq* file with failed reads. This utility is conveniet for *multiple filtering* of the same *input .fastq file*.

## Homework1

Utility [hw1_Collections.py](hw1_collections/hw1_Collections.py) provides some basic tools for working with *nucleic acid sequences*. Based on python dictionaries and the complementarity principle, 
this script allows to make complement sequences for DNA and RNA, to reverse them, and to transcribe RNA sequence from DNA template. 
For your convenience **hw1_collections.py** is not case-sensitive, and all charachters in output sequences in accordance with input register.