

def ms(l, first, last):
	if not last > first:
		return
	print "HERE"
	print "LAST", last
	print "FIRST", first
	mid = first + (last - first)/2
	ms(l, first, mid)
	ms(l, mid+1, last)
	merge(l, first, mid, last)


def merge(l, first, mid, last):
	temp = []
	i = first
	j = mid


	while i < mid or j < last:
		print "ALIST", alist
		print "TEMP", temp
		print "L", l[first:last]
		print "I", i
		print "J", j
	
		if i >= mid:
			temp.append(l[j])
			j += 1
		elif j >= last:
			temp.append(l[i])
			i += 1
		elif l[i] < l[j]:
			temp.append(l[i])
			i += 1
		else:
			temp.append(l[j])
			j += 1

	l[first:last] = temp


alist = [54,26,93,17,77,31,44,55,20]
ms(alist, 0, len(alist))
print(alist)

	
