from tace16 import tace16
from collections import Counter
from glob import glob
from pprint import pprint, pformat
from tqdm import tqdm
import string
import re


import logging

import numpy as np
import cairo
import math

import matplotlib.pyplot as plt
import numpy as np

import tamil



FORMAT_STRING = "%(levelname)-8s:%(name)-8s.%(funcName)-8ss>> %(message)s"
logging.basicConfig(format=FORMAT_STRING)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

characters = Counter()
lines = []
with open('length_words_first.cleaned.txt') as f:

    for lineno, line in enumerate(f.readlines()):
        removables =['‘‘', '…', '”', '’', '—', '‘', '❤️','✯', '卐',
                     
                     '\u200b', '\u200c', '\u200d',
                     '\ufeff', '\ue38d', '\u202c', '\u202a', '\ue216']
        for c in removables:
            line = line.replace(c, '')
        
        #log.info('processing {}'.format(line))
        #print(lineno, list(line))
        letters = [i for i in tamil.utf8.get_letters(line) if tamil.utf8.istamil(i)]
        characters.update(letters)
        lines.append(letters)

    pprint(characters)
    pprint(sum(characters.values()))
    characters = sorted(list(characters.keys()))
    char_len = len(characters)
    char2idx = {v:k for k, v in enumerate(characters)}
    
    heat = np.ones([char_len, char_len])

    for line in lines:
        for a, b in zip(line, line[1:]):
            #if tamil.utf8.istamil(a) and a in char2idx and b in char2idx:
            if tamil.utf8.istamil(a):
                a, b = char2idx[a], char2idx[b]
                heat[a][b] += 1


from matplotlib.font_manager import FontProperties
tamil_font150 = FontProperties(fname = '/usr/share/fonts/truetype/noto/NotoSansTamilUI-Regular.ttf', size=150)
tamil_font12 = FontProperties(fname = '/usr/share/fonts/truetype/noto/NotoSansTamilUI-Regular.ttf', size=12)

fig = plt.figure(figsize=(50, 50))

plt.imshow(
    np.log(heat)#/numpy.sum(np.log(heat), axis=1)),

,cmap='hot'
   )

plt.xticks(range(char_len), characters, fontproperties=tamil_font12, rotation='vertical')
plt.yticks(range(char_len), characters, fontproperties=tamil_font12)
plt.suptitle(u'தமிழ் எழுத்துகள்', fontproperties=tamil_font150)
plt.savefig('heatmap.png')
print(characters)



