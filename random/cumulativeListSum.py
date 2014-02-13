def cumulativeListSum(l):
	newList = list(l)
	for i in range(0,len(l)-2):
		newList[i] = l[i] + l[i+1]
	return newList

