
### Binary search on an Orderd list


l = [2,6,8,10,12,30,67,90]

def rbs(l, item):
	print l
	if len(l) == 0:
		return False
	if l[len(l)/2] == item:
		return True
	elif l[len(l)/2] > item:
		return rbs(l[:len(l)/2], item)
	else:
		return rbs(l[len(l)/2+1:], item)


def wbs(l, item):
	first = 0
	last = len(l)
	while first < last:
		mid = first + (last -first)/2
		print "First", first
		print "Last", last
		print "Mid" ,mid
		if l[mid] == item:
			return True
		elif l[mid] > item:
			last = mid - 1
		else:
			first = mid + 1
	return False
		

print rbs(l, 89)	
print wbs(l, 89)	
