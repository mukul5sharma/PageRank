The zip cantains the following files : 

PageRank.py
#This is the solution for first part of the assignment 

input : sample.txt file
output : VAlues for total 1, 10 and 100 iterations 
Execution: python PageRank.py <sample.txt>
#The loop control varible "i" inside the program
can be chaged to get the number of iterations as 1,10, 100

question1.txt
This file contains the output after 1, 10 and 100 
iterations of the pseudocode given in the assignment 
description on the provided sample.txt file.
|-----------------------------------------------------------------

PageRank2.py
#This is the solution for second part of the assignment 
input : wt2g_inlinks.txt file
output : List of all newly calculated pagerank values 
for the pages provided in the file.
Execution: python PageRank2.py <wt2g_inlinks.txt>

question2.txt
This file contains the output of the program that is a 
list of all the calculated page ranks for upto 4 consecutive 
iterations
|-----------------------------------------------------------------

PageRank3.py
#This is the solution for third part of the assignment 
input  : wt2g_inlinks.txt file
output : 
	- a list of the document IDs of the top 50 pages as 
	  sorted by PageRank
	- a list of the document IDs of the top 50 pages 
	  by in-link count, together with their in-link counts
	- the proportion of pages with no in-links (sources)
	- the proportion of pages with no out-links (sinks); and
	- the proportion of pages whose PageRank is less than 
	  their initial, uniform values. 

Execution: python PageRank3.py <wt2g_inlinks.txt>

question3.txt
This file contains the output of the program 


Question4.pdf
#This file consists of brief analysis of all the pages
which have high page rank and inlinks count values