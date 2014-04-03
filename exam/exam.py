def sum_squares(n):
	total = 0
	while n > 0:
		if n%2 == 0: #if even
			total += n**2
		n = n - 1
	return total

def pair_to_list_dictionary(l):
	d = {}
	end = len(l)
	i = 0
	while i <= end-2:
		d[l[i]] = l[i+1]
		i += 2
	return d

def split_dictionary(d):
	upperD = {}
	lowerD = {}
	for element in d:
		if element.isupper():
			upperD[element] = d[element]
		else:
			lowerD[element] = d[element]

	return [upperD,lowerD]

def in_language(s):
	numA = numB = 0
	for element in s:
		if element == 'a':
			numA += 1
		if element == 'b':
			numB += 1
	if numA == numB:
		return True
	else:
		return False	

def get_proportion(nucleotides):
	numA = numT = numC = numG = 0
	for base in nucleotides:
		if base == 'A':
			numA += 1.0
		elif base == 'T':
			numT += 1.0
		elif base == 'C':
			numC += 1.0
		elif base == 'G':
			numG += 1.0
	total = numA + numT + numC + numG
	d = {'A':numA/total,'T':numT/total,'C':numC/total, 'G':numG/total}
	return d