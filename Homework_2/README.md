# Fastq Filtrator :passport_control:
## Homework2
Utility **fastq_filtrator.py** deals with **.fastq files**. It opens *input .fastq file*, calculates *Q-score*, *GC-content*, and *length* 
for every read in file. According to calculated read *Q-score*, *GC-content*, and *length*, it performs **three types of read filtering** using values of 
```_bound``` variables. As the result, **fastq_filtrator.py** creates *_passed.fastq* file with passed reads using your ```output_file_prefix```. 
If you pass to ```save_filtered``` variable boolean ```True```, it also allows to generate *_failed.fastq* file with failed reads. 
This utility is conveniet for *repetitive filtering* of the same *input .fastq file*. Here some **guidelines** for *how to use it* and *how does it work*.

### **How to use it**
The master function ```main()``` recieves *six variables*:
- ```input_fastq``` (str): path to .fastq file
- ```output_file_prefix``` (str): first part of the output file(s) name(s)
- ```save_filtered``` (bool): variable for decision about failed reads (```True``` for saving them into '_failed.fastq' 
  file or not). Default is boolean ```False```
- ```gc_bounds``` (int, float, tuple, list): threshold(s) for read GC-content test. Default is (0, 100), single 
  int or float in ```gc_bounds``` is accepted as max boundary.
- ```length_bounds``` (int, tuple, list): threshold(s) for read length test. Default is (0, 2**32), single int
    in ```length_bounds``` is accepted as max boundary.
    *Attention! ```length_bounds``` can't be ```float```!*
- ```quality_threshold``` (int): threshold for read quality test. Default is 0

### **How does it work**
The **fastq_filtrator.py** provides **three parameters calculations** for every read in *input .fasta file*. They are read *Q-score*, *GC-content*, and *length*. 
For their determination and testing, function ```main``` calls other *functions* and accepts ```_bound``` variables as thresholds. These fuctions listed bellow.

*Functions* for calculations and testing:
- ```qscore_filter()```: calculates *Q-score* for every read in *input .fastq file*. It decodes each nucleotide quality given in ASCII format into 
*numeric Phred33 format* and determines mean value for read. After calculations function checks, whether *read quality* meets ```quality_threshold```
- ```gc_content_filter()```: calculates *percentage of GC nucleotides* for every read in *input .fastq file*. After calculations function checks, 
whether *GC-content* meets ```gc_bounds```
- ```length_filter()```: calculates *length* for every read in *input .fastq file*. After calculations function checks, whether read length meets ```length_bounds```

Also function ```main()``` uses fuction ```get_read()``` getting **one read** (four strings) from *input .fastq file* and returns it in ```list``` format. 
Function ```output_generator``` generates one or two *output .fastq file(s)* with reads from *input .fastq file* after their filtering. 
It creates *_passed.fastq file* with passed reads using ```output_file_prefix```. If you choosed ```True``` for ```save_filtered``` variable, 
it will also generates *_failed.fastq file* with failed reads.   

For *repetitive filtering* of the same *input .fastq file* with different filtering parameters, **fastq_filtrator.py** imports standart Python ```os``` module and 
removes *output .fatsq* files with ```output_file_prefix```, if they are pre-existed. If you need to collect all *output .fastq file*, 
use different ```output_file_prefix```for every **fastq_filter.py** usage.
