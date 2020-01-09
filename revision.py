import sys
import os
from collections import Counter
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import shutil
import scipy as sp
from scipy.spatial import distance



def makegraph(word_list, name):


word_list = []
directory_list = []
directory_mean = 0
JSDVALUES = []
SingleLabels = []
JSDlist = []
jsdmean = []
jsdmeanlabels = []
scatterPoints = []
meanflag = 0
base_dir = os.getcwd()
temp = []
directory_word_list = []
word_list_array = []
names = []

Dirs = sys.argv[1:]
Dirs_1 = []

#directory list
for i in Dirs:
    Dirs_1.append(os.path.join(base_dir, i))
path = base_dir


for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file and r in Dirs_1:
                #print(r)
                oof = file.split('.')
                name = oof[0] + '_hist.png'
                names.append(name)
                #files.append(os.path.join(r, file))
                with open(os.path.join(r, file), "r") as g:
                    for line in g:
                        for word in line.split():
                            if word.isalpha() and word not in word_list:
                                word_list.append(word)
                            if word.isalpha() and word not in directory_word_list:
                                directory_word_list.append(word)
                    word_list_array.append(word_list)




            for i in range(0, len(word_list_array)):
                makegraph(word_list_array[i], names[i],len(word_list_array)):


            directory_word_list *= 0
            word_list_array *= 0
