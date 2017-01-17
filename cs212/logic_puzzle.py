"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""


import itertools

def logic_print():
    days = (monday, tuesday, wednesday, thursday, friday) = (0, 1, 2, 3, 4)
    ordering = list(itertools.permutations(days))
    
    return next((Hamming, Knuth, Minsky, Simon, Wilkes)
        for (Hamming, Knuth, Minsky, Simon, Wilkes) in ordering
        for (laptop, droid, tablet, iphone, _) in ordering
        if wednesday == laptop
        for (programmer, writer, manager, designer, __) in ordering
        if programmer !=  Wilkes
        if (Wilkes == programmer and Hamming == droid) or (Wilkes == droid and Hamming == programmer)
        if writer != Minsky
        if Knuth != manager and tablet != manager
        if Simon+1 == Knuth
        if thursday != designer
        if friday != tablet
        if designer != droid
        if manager+1 == Knuth
        if (laptop == monday and Wilkes == writer) or (laptop == writer and Wilkes == monday)
        if iphone == tuesday or tablet == tuesday
        )

people = ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

def logic_puzzle():
	retList = [0] * 5
	i = 0
	for index in logic_print():
		retList[index] = people[i]
		i += 1
	return retList

#print logic_print()
	
		




