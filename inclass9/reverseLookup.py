def reverseLookup(d,v):
	returnList = []
	for k in d:
		if d[k] == v:
			returnList.append(k)
	return(returnList)

