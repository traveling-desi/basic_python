# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!



def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    if text == '':
	return (0,0)
    palList = []
    text = text.lower()
    for i in range(1, len(text)-1):
	if text[i-1] == text[i+1]:
		palList.append(find_palindrome(text, i-1, i+1))
	elif text[i-1] == text[i]:
		palList.append(find_palindrome(text, i-1, i))
	elif text[i] == text[i+1]:
		palList.append(find_palindrome(text, i, i+1))

    palList = sorted(palList, reverse = True, key=palDistance)
    return palList[0]
  

def find_palindrome(text, i, j):
	while i >=0 and j < len(text) and text[i] == text[j]:
		j += 1
		i -= 1
	return (i+1, j)

def palDistance( (i,j) ):
	return j-i 

	
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    assert L('') == (0, 0)
    return 'tests pass'

print test()
#text = 'Mad am I ma dam'
#text = text.lower()
#print len(text)
#print text[8]
#print find_palindrome(text, len(text)/2)
