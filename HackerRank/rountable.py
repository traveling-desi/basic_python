'''
Objective 
In this challenge, we practice calculating probability.

Task 
There are  people about to sit down around a round table. Find the probability that  particular people will sit next to one another.

'''


import itertools
from fractions import Fraction

people = [1,2,3,4,5,6,7,8,9,10]

tables = itertools.permutations(people)

b = [table for table in tables if abs(table.index(1) - table.index(2)) in [1,9]]
tables = itertools.permutations(people)

b_len = len(b) * 1.0
table_len = len(list(tables))
ans = b_len/table_len
print Fraction.from_float(ans)

