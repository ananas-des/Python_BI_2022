# Internet :ramen:

## Homework11

Here some solutions for Python **Internet** Tasks using `requests`, `bs4`, `re`, `io`, `python-dotenv`, and other modules.

### System
This code was tested on **Ubuntu 22.04.1 LTS** with **Python version 3.9.13**.

*Note: for this Homework built-in Python packages and `bs4`, `python-dotenv`, `matplotlib`, and `seaborn`modules were used.*

### Files
In this directory there are *four files*: [README.md](./README.md), [hw11_internet.ipynb](./hw11_internet.ipynb), [hw11_internet.py](./hw11_internet.py), [genscan_api.zip](./genscan_api.zip) and [requirements.txt](./requirements.txt).

- **README.md**: discriptions for files in this directory 
- **requirements.txt**: .txt file with environment dependencies
- **hw11_internet.ipynb**: jupyter notebook with Tasks solutions
- **hw11_internet.py**: .py file with only code from jupyter notebook
- **genscan_api.zip**: archive with files for GENSCAN Python API

### Folders

In [genscan_api](./genscan_api) folder there are [genscan_api.py](./genscan_api/genscan_api.py) .py script with *Python API* for [GENSCAN](http://hollywood.mit.edu/GENSCAN.html) web tool, [example_sequence.txt](./genscan_api/example_sequence.txt) with example gene sequence input, [requirements.txt](./genscan_api/requirements.txt) with its environment dependencies.

## Task1. Top 250 IMDb film list

- parse [Top 250 IMDb film list](https://www.imdb.com/chart/top/?ref_=nv_mp_mv250) to obtain certain information from web page

## Task2. Telegram logger

- create decorator `telegram_logger` for calculating function exacution time, creating .log file, and sending it to Telegram bot

## Task3. GENSCAN API

- create Python API for [GENSCAN](http://hollywood.mit.edu/GENSCAN.html) web tool

### GENSCAN API Usage

Use [genscan_api.py](./genscan_api/genscan_api.py) as the Python module:

- download [genscan_api.zip](./genscan_api.zip) API archive, unzip it and navigate into it:

```
$ wget https://github.com/ananas-des/Python_BI_2022/blob/Homework_11/Homework_11/genscan_api.zip
$ unzip genscan_api.zip
$ cd genscan_api
```

- create virtual environment

`$ conda create --name {env name} python=3.9.13`

- activate you virtual environment

`$ conda activate {env name}`

- install the specified packages using the configuration file [requirements.txt](./genscan_api/requirements.txt)

`$ pip install -r requirements.txt`

- run your main program and import **genscan_api.py** as module. Here an example of module usage with sequence input

```
import genscan_api as gs

sequence = '''GAAAAGGAGAGAAGAGGAGGGGAAGGAAGAAAAAGGGAAGGAGAAGAAAGAAAAGCAAACATGAAGATAA
ACACTTCAATATATGATATCCCAAGACCATCTACCCTTTTGTAAAAATTTTGCTTTTTTTTTTTCCCCCC
CAAGAGTCAGGGTCTCACTCTGTCGCCCAGGCTAGAGTGCAGTGCCATGAACATAACTCACTGTAGCCTC
TAACTCCGGGGCTCAAGCAATCCTCCTGCCTCAGCCTCCTGGGTAGCTGGGACTACAGGCATGCACCACC
ACATCTGGCTATTATTATTATTACTATATTAGTAGAGATGGGGTCTTTCTATGTTGCCTAGGCTGGTCTC
AAATTCCTGGCCTCAAGCAATTCTTCCACCTCACATTGGCCTTCCAAAGTGCTGGGATTACAATAAGCCA
CCATAGGCCAAAATTTTGCATTTTATCCATTACTGTAAAATTAACCCTTAGAAATCCAACAACACTCAAT ...
'''

gs.run_genscan(sequence=sequence)
```

and sequence_file input

```
sequence_file = "example_sequence.txt"
gs.run_genscan(sequence_file=sequence_file)
```

Output for [example_sequence.txt](./genscan_api/example_sequence.txt):
*Notes:* 
1) your sequence file should contain only gene sequence due to GENSCAN parsing specificities;
2) for `Print options` *Predicted CDS and peptides* is specified;
3) `GenscanOutput` object attributes `cds_list` and `peptide_list` contain predicted CDS (nucleotide sequences) and peptide sequences, respectively

```
GenscanOutput:
    status: 200
    exon_list: [SeqChunk(id_=1.01, type_=Init, start=2348, stop=2387), SeqChunk(id_=1.02, type_=Intr, start=3053, stop=3073), SeqChunk(id_=1.03, type_=Intr, start=3406, stop=3663), SeqChunk(id_=1.04, type_=Intr, start=7126, stop=7383), SeqChunk(id_=1.05, type_=Term, start=8885, stop=9072)]
    intron_list: [SeqChunk(id_=1.01, type_=Intron, start=2388, stop=3052), SeqChunk(id_=1.02, type_=Intron, start=3074, stop=3405), SeqChunk(id_=1.03, type_=Intron, start=3664, stop=7125), SeqChunk(id_=1.04, type_=Intron, start=7384, stop=8884)]
    cds_list: [FastaRecord(id_='GENSCAN_predicted_CDS_1', length='765_bp', seq='atgtggcagctgctcctcccaactgctctgctacttctagtttcagctggcatgcggactgaagatctcccaaaggctgtggtgttcctggagcctcaatggtacagggtgctcgagaaggacagtgtgactctgaagtgccagggagcctactcccctgaggacaattccacacagtggtttcacaatgagagcctcatctcaagccaggcctcgagctacttcattgacgctgccacagtcgacgacagtggagagtacaggtgccagacaaacctctccaccctcagtgacccggtgcagctagaagtccatatcggctggctgttgctccaggcccctcggtgggtgttcaaggaggaagaccctattcacctgaggtgtcacagctggaagaacactgctctgcataaggtcacatatttacagaatggcaaaggcaggaagtattttcatcataattctgacttctacattccaaaagccacactcaaagacagcggctcctacttctgcagggggctttttgggagtaaaaatgtgtcttcagagactgtgaacatcaccatcactcaaggtttggcagtgtcaaccatctcatcattctttccacctgggtaccaagtctctttctgcttggtgatggtactcctttttgcagtggacacaggactatatttctctgtgaagacaaacattcgaagctcaacaagagactggaaggaccataaatttaaatggagaaaggaccctcaagacaaatga')]
    peptide_list: [FastaRecord(id_='GENSCAN_predicted_peptide_1', length='254_aa', seq='MWQLLLPTALLLLVSAGMRTEDLPKAVVFLEPQWYRVLEKDSVTLKCQGAYSPEDNSTQWFHNESLISSQASSYFIDAATVDDSGEYRCQTNLSTLSDPVQLEVHIGWLLLQAPRWVFKEEDPIHLRCHSWKNTALHKVTYLQNGKGRKYFHHNSDFYIPKATLKDSGSYFCRGLFGSKNVSSETVNITITQGLAVSTISSFFPPGYQVSFCLVMVLLFAVDTGLYFSVKTNIRSSTRDWKDHKFKWRKDPQDK')]
```