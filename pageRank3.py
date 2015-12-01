__author__ = 'Mukul'

import sys
from collections import defaultdict
import math
import operator

P = set()            #set of all unique pages
m = defaultdict(set) #pages that link to a particular page
l = defaultdict(set) #out links
pr = {}              #set of page ranks
newPr = {}           #new page ranks
sinkNodes = set()    #set of all sink nodes
N = 0                #total number of nodes
d = 0.85             #teleportation factor
totalSinks = 0       #the number of pages with no in-links (sources)
totalSources = 0     #the number of pages with no out-links (sinks)
lessPr = 0           #pages whose PageRank is less than their initial, uniform values
i = 1                #Control variable for iteration
count = 0

#perplexity
def calculatePerplexity(page_rank):
    perplexity = 0
    entropy = 0
    for v in page_rank.values():
        entropy += v *math.log(1/v, 2)
    perplexity = math.pow(2, entropy)

    return perplexity

#Open file
f = open(sys.argv[1], 'r')

#Process file for extracting data
for line in f:
    N += 1
    lineItems = line.strip().split(" ")
    P.add(lineItems[0])
    #Populate inlinks and outlinks lists
    for item in lineItems[1:]:
        m[lineItems[0]].add(item)
        l[item].add(lineItems[0])

f.close()

#initialize page rank
for p in P:
    pr[p] = 1/float(N)

#sink nodes
for p in P:
    if len(l[p]) == 0:
        sinkNodes.add(p)
        totalSinks += 1
    if len(m[p])== 0:
        totalSources += 1

prevPerplexity = 0
newPerplexity = calculatePerplexity(pr)

#Pseudocode implementation
while i!=5:
    if(abs(int(newPerplexity)-int(prevPerplexity))==0):
        i += 1
        #print i
    else:
        i=0
    #print newPerplexity
    count +=1

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

#For calculating proportion of pages whose rank is less than the original rank
for entity in P:
    if(pr[entity]<(1/float(N))):
        lessPr += 1

#sorting
#page rank
sortedPr = {}
sortedPr = sorted(pr.items(), key=operator.itemgetter(1),reverse=True)
rankNum = 0

#print sortedPr
print "\nA list of the document IDs of the top 50 pages as sorted by PageRank, together with their PageRank values:"
for r in sortedPr:
    print r
    rankNum += 1
    if(rankNum > 50):
        break

#in links
#calculate number of inlinks
mLinksCount = {}
for page in P:
    mLinksCount.update({page:len(m[page])})

sortedMlinks = {}
sortedMlinks = sorted(mLinksCount.items(),key=operator.itemgetter(1),reverse=True)

linkNum = 0
print "\nA list of the document IDs of the top 50 pages by in-link count, together with their in-link counts:"
for k in sortedMlinks:
    print k
    linkNum += 1
    if(linkNum>50):
        break

#Calculate and print proportions
sourcesPro = totalSources/float(N)
sinksPro = totalSinks/float(N)
rankPro = lessPr/float(N)

print "\nThe proportion of pages with no in-links (sources)"
print sourcesPro
print "\nThe proportion of pages with no out-links (sinks)"
print sinksPro
print "\nThe proportion of pages whose PageRank is less than their initial, uniform values."
print rankPro