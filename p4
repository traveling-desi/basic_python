# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(a, b):
    b_r = b[::-1]
    a_r = a[::-1]
    x = a_r.find(b_r) 
    if x == -1:
        return x
    else:
        return len(a_r) - x - len(b_r)
    




print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

#print find_last('aaaa', 'b')
#>>> -1

#print find_last("111111111", "1")
#>>> 8

#print find_last("222222222", "")
#>>> 9

#print find_last("", "3")
#>>> -1

#print find_last("", "")
#>>> 0


