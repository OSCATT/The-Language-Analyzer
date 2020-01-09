#File: investigate.py
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

def jsd(p, q, base=np.e):

    ## convert to np.array
    p, q = np.asarray(p), np.asarray(q)
    ## normalize p, q to probabilities
    p, q = p/p.sum(), q/q.sum()
    m = 1./2*(p + q)
    return sp.stats.entropy(p,m, base=base)/2. +  sp.stats.entropy(q, m, base=base)/2.

def makegraph(word_list_1, name):

    length = len(word_list_1)
    counts = Counter(word_list_1)
    #print(counts)
    labels, values = zip(*counts.items())

    indSort = np.argsort(values)[::-1]
    #print(indSort)

    labels = np.array(labels)[indSort]
    values = np.array(values)[indSort]

    indexes = np.arange(len(labels))

    #FORMAT FOR ---PROBABLILITY---
    newVal = []
    for i in values:
        newVal += [float(i)/length]



    if meanflag == 1:
        jsdmean.extend(newVal)
        jsdmeanlabels.extend(labels)
    else:
        JSDVALUES.append(newVal)
        SingleLabels.append(labels)

    #print(newVal)

    bar_width = 0.2

    plt.xlabel("Distribution Percentage",fontsize = 13)
    plt.ylabel("Word",fontsize = 13)
    plt.title(oof[0] + "_hist")

    if meanflag == 1:
        plt.title("summary_meanDist")
    plt.barh(indexes, newVal)

    # add labels
    plt.yticks(indexes + bar_width, labels)


    plt.savefig(name)
    #print("moving" + (os.path.join(base_dir,name)) + "-----TO----- " + r)
    dest = shutil.move((os.path.join(base_dir, name)), (os.path.join(r, name)))
    plt.clf()

    #word_list_1 *= 0
    counts = []
    values *= 0
    length = 0


#start of code



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


Dirs = sys.argv[1:]
Dirs_1 = []
for i in Dirs:
    Dirs_1.append(os.path.join(base_dir, i))
path = base_dir

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file and r in Dirs_1:
                #print(r)
                oof = file.split('.')
                name = oof[0] + '_hist.png'

                #files.append(os.path.join(r, file))
                with open(os.path.join(r, file), "r") as g:
                    for line in g:
                        for word in line.split():
                            if word.isalpha():
                                word_list.append(word)
                    print("Making Histogram for " + file)
                    #print("file length - " + str(float(len(word_list))))
            #for each file in a directory create a larger list of words with all. also keep track of how many files
                    makegraph(word_list_1 = word_list, name = name)
                directory_list.extend(word_list)
                word_list *= 0
                directory_mean += 1
            #print(directory_list)

        if directory_mean > 0:
            print("Making Histogram for entire directory" )

            meanflag = 1
            makegraph(word_list_1 = directory_list, name = "summary_meanDist.png")
            meanflag = 0
            directory_list *= 0
            directory_mean =0


            #find the jsd array, indices which match
            for h in range (0, len(SingleLabels)):

                for i in range(0,len(SingleLabels[h])):
                    for j in range(0, len(jsdmeanlabels)):
                        #compare if the words are the same, then append corresponding value to an array
                        if jsdmeanlabels[j] == SingleLabels[h][i]:
                            temp.append(jsdmean[i])
                #print(temp)
                JSDlist.extend(temp)

                str = distance.jensenshannon(JSDVALUES[h],JSDlist)
                scatterPoints.append(str)

                temp*= 0
                JSDlist *= 0
                #JSDVALUES *= 0
                #jsdmean *= 0
            print("SCATTERPLOT POINTS")
            print(scatterPoints)

            x = np.array(scatterPoints)
            y = np.array(scatterPoints)
            colors = (0,0,0)
            area = np.pi*3

            # Plot
            plt.scatter(x, y, s=area, c=colors, alpha=0.5)
            plt.title('jensenshannon_distances')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.savefig("jensenshannon_distances")
            name = "jensenshannon_distances.png"
            dest = shutil.move((os.path.join(base_dir, name)), (os.path.join(r, name)))
            plt.clf()
        JSDlist *= 0
        temp*= 0
        jsdmean *= 0
        jsdmeanlabels *=0
        JSDVALUES *= 0
        SingleLabels *= 0
        scatterPoints *=0



#for f in files:
#    print(f)
