'''
Objective 
In this challenge, we practice calculating probability.

Task 
Bag  contains  white balls and  black balls. Bag  contains  white balls and  black balls. You draw  ball from bag  and, without observing its color, put it into bag . Now, if a ball is drawn from bag , find the probability that it is black.
'''



import random
from fractions import Fraction

x = ['w']* 5 + ['b'] * 4
y = ['w']* 7 + ['b'] * 6

num_trials = 1000000
trials = num_trials
result = 0

while trials > 0:
	y_new = y + [random.choice(x)]
	ball = random.choice(y_new)
	if ball == 'b':
		result += 1
	trials -= 1

#ans = "%.2f" % (result*1.0/num_trials)
#print Fraction(ans)

print (result*1.0/num_trials)
print 29.0/63

		


