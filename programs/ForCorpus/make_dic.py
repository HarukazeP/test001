# -*- coding: utf-8 -*-


from __future__ import with_statement
import re
import sys
import datetime
from keras.utils.data_utils import get_file
import numpy as np
import re

today=datetime.datetime.today()
print('all_start = ',today)

#path = './corpus/miniWiki.txt'
path = get_file('nietzsche.txt', origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt')

'''
###メモリ抑える方
all_words=[]
i=0
with open(path,'r') as f:
    for line in f:
        i+=1
        if(i<20):
            print('line:', i)       
        if(i%1000==0):
            print('line:', i)
        line=line.lower()
        line = line.replace("\n", " ")
        line = re.sub(r"[^a-z ]", "", line)
        line = re.sub(r"[ ]+", " ", line)
        line_list = line.split(" ")
        line_words=list(set(line_list))
        all_words.append(line_words)
        all_words=[x for i, x in enumerate(all_words) if i == all_words.index(x)]

today=datetime.datetime.today()
print('read_end = ',today)

all_words = sorted(all_words)
print('kind of words:', len(all_words))
'''
###メモリ贅沢に使う方
text = open(path).read().lower()
text = text.replace("\n", " ")
text = re.sub(r"[^a-z ]", "", text)
text = re.sub(r"[ ]+", " ", text)
today=datetime.datetime.today()
print('read_end = ',today)

text_list=text.split(" ")
print('todal words:', len(text_list))
all_words = sorted(list(set(text_list)))
print('kind of words:', len(all_words))
####


with open('./corpus/wiki_words_test.txt','w') as f2:
    for x in all_words:
        f2.write(str(x)+" ")

today=datetime.datetime.today()
print('all_end = ',today)