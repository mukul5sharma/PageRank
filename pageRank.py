__author__ = 'Mukul'

import sys
from collections import defaultdict

P = set()            #set of all unique pages
m = defaultdict(set) #pages that link to a particular page
l = defaultdict(set) #out links
pr = {}              #set of page ranks
newPr = {}           #new page ranks
sinkNodes = set()    #set of all sink nodes
N = 0                #total number of nodes
d = 0.85             #teleportation factor
i = 1                #Number of iterations

#open file
f = open(sys.argv[1], 'r')

#process file for extracting data
for line in f:
    lineItems = line.split(" ")
    #add to the list of unique pages
    P.add(lineItems[0])
    N += 1

    #Populate inlinks and outlinks lists
    for item in lineItems[1:]:
        m[lineItems[0]].add(item)
        l[item].add(lineItems[0])

f.close()

#Initialize page rank default values
for p in P:
    pr[p] = 1/float(N)

#Sink nodes
for p in P:
    if len(l[p]) == 0:
        sinkNodes.add(p)


#----Pseudocode implementation----#

# Upper limit of "i" can be 1, 10 or 100
while i<=1:
    sinkPr = 0

    for sPage in sinkNodes:
        sinkPr += pr[sPage]

    for page in P:
        #calculate new page rank values
        newPr[page] = (1-d)/(N)
        newPr[page] += ((d*sinkPr)/N)
        for q in m[page]:
            if q in P:
                newPr[page] += (d*pr[q]/len(l[q]))

    #change with new page rank values
    for n in P:
        pr[n] = newPr[n]

    i += 1

#Print all newly calculated values for page rank
print pr
