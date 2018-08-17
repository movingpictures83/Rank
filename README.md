# Rank
# Language: Python
# Input: CSV (set of samples and measurements)
# Output: CSV (set of samples and ranks)
# Tested with: PluMA 1.0, Python 2.7

PluMA plugin that takes as input a CSV file with rows representing
samples and columns representing entities.  Entry (i, j) represents
the abundances of entity j in sample i.

It will produce a CSV file where entry (i, j) corresponds to the rank
of entity j in sample i with respect to abundance (1 being the highest).

As a simple example, the following input:

"","A","B","C"
"1",10,3,5
"2",5,8,1

would produce:

"","A","B","C"
"1",1,3,2
"2",2,1,3
