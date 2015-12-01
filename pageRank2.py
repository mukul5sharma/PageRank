__author__ = 'Mukul'

import sys
from collections import defaultdict
import math

P = set()            #set of all unique pages
m = defaultdict(set) #pages that link to a particular page
l = defaultdict(set) #out links
pr = {}              #set of page ranks
newPr = {}           #new page ranks
sinkNodes = set()    #set of all sink nodes
N = 0                #total number of nodes
d = 0.85             #teleportation factor
i = 1                #Control variable for iteration
count = 0

#Perplexity
def calculatePerplexity(page_rank):
    perplexity = 0
    entropy = 0
    for v in page_rank.values():
        entropy += v *math.log(1/v, 2)
    perplexity = math.pow(2, entropy)

    return perplexity

#open file
f = open(sys.argv[1], 'r')

#process file for extracting data
for line in f:
    N += 1
    lineItems = line.strip().split(" ")
    P.add(lineItems[0])
    #Populate inlink and outlink lists
    for item in lineItems[1:]:
        m[lineItems[0]].add(item)
        l[item].add(lineItems[0])

f.close()

#Initialize page rank
for p in P:
    pr[p] = 1/float(N)

#sink nodes
for p in P:
    if len(l[p]) == 0:
        sinkNodes.add(p)

prevPerplexity = 0
newPerplexity = calculatePerplexity(pr)

#Pseudocode implementation
while i<5:
    if(abs(int(newPerplexity)-int(prevPerplexity))==0):
        i += 1
        print i
    else:
        i = 0

    print newPerplexity
    count += 1

    sinkPr = 0
    for sPage in sinkNodes:
        sinkPr += pr[sPage]

    for page in P:
        newPr[page] = (1-d)/(N)
        newPr[page] += d*sinkPr/N
        for q in m[page]:
            newPr[page] += d*pr[q]/len(l[q])

    for n in P:
        pr[n] = newPr[n]

    prevPerplexity = newPerplexity
    newPerplexity = calculatePerplexity(newPr)

#print count