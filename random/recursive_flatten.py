def recursive_flatten(l):
	""" 
	Takes in a list of nested lists, and returns a single list not containing any lists
	"""
	resultList = []

	for item in l:
		if type(item) == list:
			newthing = recursive_flatten(item)
			print 'recursing' + str(newthing)
			resultList += newthing
		else:
			resultList.append(item)

	return resultList

