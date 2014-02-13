def nestedSum(l):
	for i in range(len(l)):
		l[i] = sum(l[i])
	return l
