#File: examine.py

import os
from collections import Counter
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import shutil
import sys
word_list = []
base_dir = os.getcwd()
entries = os.listdir(base_dir)

Dirs = sys.argv[1:]
Dirs_1 = []
for i in Dirs:
    Dirs_1.append(os.path.join(base_dir, i))


path = base_dir

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file and r in Dirs_1:
            oof = file.split('.')
            #print( oof[0] + '.txt' )
            #files.append(os.path.join(r, file))
            with open(os.path.join(r, file), "r") as g:
                for line in g:
                    for word in line.split():
                        if word.isalpha():
                            word_list.append(word)

            length = len(word_list)
            #print(length)

            counts = Counter(word_list)
            #print(counts)
            labels, values = zip(*counts.items())



            # sort your values in descending order
            indSort = np.argsort(values)[::-1]
            #print(indSort)


            # rearrange your data
            labels = np.array(labels)[indSort]
            values = np.array(values)[indSort]

            indexes = np.arange(len(labels))

            #FORMAT FOR ---PROBABLILITY---
            newVal = []
            for i in values:
                newVal += [float(i)/length]

            #print(newVal)

            bar_width = 0.2

            plt.xlabel("Distribution Percentage")
            plt.ylabel("Word")

            plt.barh(indexes, newVal)


            # add labels
            plt.yticks(indexes + bar_width, labels)

            #plt.show()

            #fig = plt.hist(a, 5, facecolor='b', ec='k', alpha=0.5)			(graph the figure)
            #plt.savefig('foo.png')
            # sort your values in descending order
            name = oof[0] + '_hist.png'
            print("Histogram made for " + file)

            plt.savefig(name)

            #print("moving" + (os.path.join(base_dir,name)) + "-----TO----- " + r)

            dest = shutil.move((os.path.join(base_dir, name)), (os.path.join(r, name)))


            plt.clf()
            word_list *= 0
            counts = []
            values *= 0
            length = 0
#for f in files:
#    print(f)
