# Repository for Python Homeworks in IB
## Homework2

Utility **fastq_filtrator.py** deals with **.fastq files**. It opens *input .fastq file*, calculates *Q-score*, *GC-content*, and *length* 
for every read in file. According to calculated read *Q-score*, *GC-content*, and *length*, it performs **three types of read filtering** using values of ```_bound``` variables. As the result, **fastq_filtrator.py** creates *_passed.fastq* file with passed reads using your ```output_file_prefix```. If you pass to ```save_filtered``` variable boolean ```True```, it also allows to generate *_failed.fastq* file with failed reads. This utility is conveniet for *multiple filtering* of the same *input .fastq file*.

## Homework1

Utility [hw1_Collections.py](hw1_collections/hw1_Collections.py) provides some basic tools for working with *nucleic acid sequences*. Based on python dictionaries and the complementarity principle, 
this script allows to make complement sequences for DNA and RNA, to reverse them, and to transcribe RNA sequence from DNA template. 
For your convenience **hw1_collections.py** is not case-sensitive, and all charachters in output sequences in accordance with input register.