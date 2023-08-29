import google
import math
from typing import Dict
from bs4 import builder, BeautifulSoup
import requests
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
import aiohttp
import pandas
import cv2


def update_dictionary(dct1: Dict, dct2: dict) -> None:
    return dct1 | dct2


dict1 = {"A": 1, "B": 2}
dict2 = {"A": 3, "C": 8}
string = f"{math.pi:.5f}"
BeautifulSoup("", "lxml")
update_dictionary(dict1, dict2)
alignments = max(pairwise2.align.globalds("ATATCTCGATCGCTACGTC", "CTAGCTCGCTGCTCAGCATC",
                                          matlist.blosum62, -10, -0.5), key=lambda x: x.score)

try:
    some_string = "abc dfg"
    match some_string.split():
        case var, "dfg":
            print("It works")
        case _:
            print("Not working")
except* ExceptionGroup:
    pass

print(alignments)
pandas.read_html("https://www.w3schools.com/html/html_tables.asp")[0]
pandas.DataFrame([1, 2, 3, 4], index={1, 2, 3, 4})
print(b'\xd0\x92\xd1\x81\xd1\x91 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xb5\xd1\x82, \xd1\x82\xd1\x8b \xd0\xb1\xd0\xbe\xd0\xbb\xd1\x8c\xd1\x88(\xd0\xbe\xd0\xb9/\xd0\xb0\xd1\x8f) \xd0\xbc\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x86!!!!'.decode("utf-8").removesuffix("!"))
