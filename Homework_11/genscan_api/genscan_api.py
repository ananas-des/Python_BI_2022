#!/usr/bin/env python


import os
import requests
import re
from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class GenscanOutput:
    '''A dataclass with GENSCAN (http://hollywood.mit.edu/GENSCAN.html) output
    
    Parameters:
        status (str): request status
        exon_list (list): list with predicted exons
        intron_list (list): list with predicted introns 
        cds_list: list with predicted CDS sequences
        peptide_list: list with predicted peptide sequences
    '''
    
    
    status: str
    exon_list: list
    intron_list: list
    cds_list: list
    peptide_list: list
    
    
    def __repr__(self):
        '''For represnting GenscanOutput object'''
        rep = f'''GenscanOutput:
    status: {self.status}
    exon_list: {self.exon_list}
    intron_list: {self.intron_list}
    cds_list: {self.cds_list}
    peptide_list: {self.peptide_list}
    '''
        return rep
    

class SeqChunk:
    '''A class with information for exon and intron'''
    
    
    def __init__(self, id_, type_, start, stop):
        self.id_ = id_
        self.type_ = type_   
        self.start = int(start)
        self.stop = int(stop)
        
    
    def __repr__(self):
        '''For representing SeqChunk object'''
        
        
        rep = f'SeqChunk(id_={self.id_}, type_={self.type_}, start={self.start}, stop={self.stop})'
        return rep
    
    
@dataclass
class FastaRecord:
    '''A dataclass with information about fasta record
    
    Parameters:
        id_ (str): record id (Seq_ID)
        description (str): record description (if exists)
        seq (str): biological sequences
    '''
    
    
    id_: str
    length: str
    seq: str

    
def run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name=""):
    '''Function run_genscan() sends request to GENSCAN web tool (http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi)
    
    Parameters:
        sequence (str): gene sequence
        sequence_file (str): path to sequence file
        organism (str): organism type, "Vertebrate", "Arabidopsis", and "Maize" are available
        exon_cutoff (float): suboptimal exon cutoff, 0.01, 0.02, 0.05, 0.1, 0.25, 0.5, and 1.00 are available
        sequence_name (str): sequence name
        
    Returns: GenscanOutput() object as the result of parse_genscan_response() function
    '''
    
    
    if (sequence and sequence_file) or (not sequence and not sequence_file):
        raise ValueError("You must choose sequence OR sequence file to load!")
    
    organisms = ["Vertebrate", "Arabidopsis", "Maize"]
    exon_cutoffs = [0.01, 0.02, 0.05, 0.1, 0.25, 0.5, 1.00]
        
    if organism not in organisms or exon_cutoff not in exon_cutoffs:
        raise ValueError(
        f'''Check values for "organism" or "exon_cutoff" parameters!
            Values for "organism": {organisms};
            Values for "exon_cutoff": {exon_cutoffs}
            '''
        )
    
    genscan_url = "http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi"    
    query_string_params = {
            "-o": organism,
            "-e": exon_cutoff,
            "-n": sequence_name,
            "-p": "Predicted CDS and peptides"
        }

    if sequence:
        query_string_params.update({"-s": sequence})
        response = requests.post(genscan_url, data=query_string_params)
    if sequence_file:
        if not os.path.isfile(sequence_file):
            raise ValueError(f'No such file {sequence_file.split(os.path.sep)[-1]}. Check path to file!')    
        with open(sequence_file,'rb') as file:
            response = requests.post(genscan_url, files={"-u": file}, data=query_string_params)
    return parse_genscan_response(response)


def parse_genscan_response(response):
    '''Function parse_genscan_response() parses resulted response from 
    GENSCAN web tool (http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi)
    
    Parameters:
        response (requests.models.Response): GENSCAN response
    
    Returns: GenscanOutput() object with parsed output from GENSCAN    
    '''
    
    
    status = response.status_code
    soup = BeautifulSoup(response.content, "lxml")
    output = soup.find('pre').text
    if re.search(r'NO EXONS/GENES PREDICTED IN SEQUENCE', output):
        raise Exception(f'Request status: {status}. No exons/genes were predicted!')
    
    content_list = output.split('\n'*5)
    table = content_list[0]

    exon_pattern = re.compile(r'([\d\.]+?)\s([^P]\w+)\s[+-]\s+?([\d]+)\s+?([\d]+)')
    exons = re.findall(exon_pattern, table)
    exon_list = [SeqChunk(*exon) for exon in exons]
    
    strand_pattern = re.compile(r'Init\s\+') 
    strand = re.search(strand_pattern, table)
    if not strand:
        exon_list = exon_list[::-1]
        
    intron_list = []
    for i in range(1, len(exon_list)):
        intron_start = exon_list[i-1].stop + 1
        intron_stop = exon_list[i].start - 1
        intron_id = exon_list[i-1].id_
        intron_list.append(SeqChunk(intron_id, "Intron", intron_start, intron_stop))
        
    fastas = content_list[-1].split('\n\n\n')
    cds_list = []
    peptide_list = []
    for fasta in fastas:
        fasta = fasta.strip().split('\n')
        _, name, length = fasta[0].split('|')
        cds = re.search(r'CDS', fasta[0])
        fasta.remove(fasta[0])
        seq = ''.join(fasta)

        record = FastaRecord(name, length, seq)
        if cds:
            cds_list.append(record)
        else:
            peptide_list.append(record)
    return GenscanOutput(status, exon_list, intron_list, cds_list, peptide_list)