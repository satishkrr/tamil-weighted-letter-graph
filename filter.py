from tace16 import tace16
from collections import Counter
from glob import glob
from pprint import pprint, pformat
from tqdm import tqdm
import string
import re
import logging

import tamil

FORMAT_STRING = "%(levelname)-8s:%(name)-8s.%(funcName)-8ss>> %(message)s"
logging.basicConfig(format=FORMAT_STRING)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

characters = Counter()

def remove_doubles(s):
    cleaned = []
    prev_char_consonant = False
    for i in s:
        if ord(i) >= 0x0BBE and ord(i) <=0x0BD7:
            if prev_char_consonant:
                cleaned.append(i)
                prev_char_consonant = False
            else:
                pass
        elif ord(i) >= 0x0B95 and ord(i) <=0x0BB9:
            cleaned.append(i)
            prev_char_consonant = True

    return ''.join(cleaned)

import networkx as nx
from networkx.drawing.nx_pydot import write_dot

G = nx.DiGraph()
f = open('lm_lengthsorted.txt').readlines()
for line in tqdm(f[:1000000]):
    for word in line.split():
        word = remove_doubles(word)
        word = ['SOW'] + tamil.utf8.get_letters(word)+ ['EOW']
        
        for a, b in zip(word, word[1:]):
            G.add_node(a)
            G.add_node(b)
            if not b in G[a]:
                G.add_edge(a, b, weight=1)
            else:
                G[a][b]['weight'] += 1

                
write_dot(G, 'graph.dot')                
"""
with open('lm_lengthsorted.txt') as f:
    for line in tqdm(f.readlines()):
        for word in line.split():
            word = remove_doubles(word)
            characters.update(tamil.utf8.get_letters(word))


    pprint(characters)
"""
