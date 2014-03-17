def exclusive_or_dict(d1,d2):
	resultingDictionaty = {}
	sameDictionary = {}
	for element in d1:
		for entry in d2:
			if element == entry:
				sameDictionary[element] = d1[element]

	
	for entry in d1:
		if entry in sameDictionary:
			print ''
		else:
			resultingDictionaty[entry] = d1[entry]

	for entry in d2:
		if entry in sameDictionary:
			print ''
		else:
			resultingDictionaty[entry] = d2[entry]
				
	return resultingDictionaty

def better_exclusive_dict(d1,d2):
	resultingDictionaty = {}
	for element in d1:
		if element not in d2:
			resultingDictionaty[element] = d1[element]
	for element in d2:
		if element not in d1:
			resultingDictionaty[element] = d2[element]

	return resultingDictionaty
