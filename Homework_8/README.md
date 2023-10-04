# **UNIX Command Copycats** :steam_locomotive:
## Homework8

**UNIX Command Copycats** are equivalent scripts for the eponymous *bash* commands. They were written using standard python modules, such as 
`os`, `sys`, `argparse` and `shutil`. Here some **guidlines** for how to *use them* and how do *they work*.


### Files
In this directory there are *nine files*: [README.md](./README.md), [copycat_scripts.zip](./copycat_scripts.zip) and *seven .py scripts* for standard *bash* commands

- **README.md**: utilities descriptions and guidelines for their usage;

- **copycat_scripts.zip**: .zip file with seven .py scripts

### System
Launch of copycat utilities was tested on **Ubuntu 22.04.1 LTS** with **Python version 3.10.6**.

### Copycap Scripts
There are discription for *seven .py scripts*. For each utility optional `-h`, or `--help` option can be used for usage information 

1. [cat.py](./cat.py): concatenate file(s) to standard output;

SYNOPSIS    `./cat.py file_path [file_path ...]`

2. [ls.py](./ls.py): lists the content of the directory in standard output;

SYNOPSIS    `./ls.py [OPTION] [file_path ...]`

  * lists *current directory* content BY DEFAULT
  
  * OPTION
    
    * **-a**, **--all** do not ignore entries starting with . (hidden files)
  
- [mv.py](./mv.py): moves or renames file(s)/directory(ies) from one path to another;

SYNOPSIS    `./mv.py file_path [file_path ...] move_to_path`

- [rm.py](./rm.py): removes files or directories

SYNOPSIS    `./rm.py [OPTION] file_path [file_path ...]`

  * OPTION
  
    * **-r**, **-R**, **--recursive** remove directories and their contents recursively

- [sort.py](./sort.py): sort lines of text files in decreasing lexicographic order

SYNOPSIS    `./sort.py file_path [file_path ...]`

- [touch.py](./touch.py): creates new file(s) in specified path if it/they does/do not already exist

SYNOPSIS    `./touch.py file_path [file_path ...]`

- [wc.py](./wc.py): prints newline, word, byte counts for each file, and a total line if more than one file is specified.

SYNOPSIS    `./wc.py [OPTIONS] file_path [file_path ...]`

  * OPTIONS
  
      * **-c**, **--bytes** print the byte counts
      
      * **-l**, **--lines** print the newline counts
      * **-w**, **--words** print the word counts

### Launch

1. Set up virtual environment

- create virtual environment
```
$ conda create --name {env name} python=3.10.6`
```
- activate you virtual environment
```
$ conda activate {env name}`
```

2. Launch scripts

- download [copycat_scripts.zip](./copycat_scripts.zip) with *seven .py scripts* using browser via [link](https://github.com/AnasZol/Python_BI_2022/raw/Homework_8/Homework_8/copycat_scripts.zip)

OR

```
$ wget https://github.com/AnasZol/Python_BI_2022/raw/Homework_8/Homework_8/copycat_scripts.zip
```

- unzip directory **copycat_scripts.zip**
```
$ unzip copycat_script.zip 
```
All the .py scripts will be in the current directory.

- make the .py scripts executable
```
$ chmod +x *.py
```

- run the files from the working directory as follows
```
$ ./<script_name.py>
```

### Pipeline structure
The script files are separated into different .py files, but can be built into the *bash shell pipeline*.

### Example workflow
```
$ ./cat.py *.txt | ./sort | ./wc.py -l
```
