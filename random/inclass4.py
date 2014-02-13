from math import sqrt

def double(n):
	return 2*n

def mysqrt(n):
	return sqrt(n)

def get_complementary_base(b):
	""" Computes the complimentary DNA base
		b:the base represented as a length 1 string
		returns: the complimentary base as a length 1 string
	"""
	if isinstance(b, basestring):
		if b == 'A' or b == "a":
			return "T"
		elif b == 'T' or b == 't':
			return "A"
		elif b == 'C' or b == 'c':
			return "G"
		elif b== 'G' or b== 'g':
			return 'C'
		else:
			print 'Incorrect Input'

	else:
		print 'incorrect type'


def sum_one_to_n(n):
	sum = 0
	for i in range(n+1):
		sum = sum + i
	return sum

def sum_one_to_n_whileloop(n):
	sum = 0
	while i <= n:
		s = s + 1
		i += 1 
	return s

def factorial(n):
	if n == 1:
		return 1
	f = 1
	for i in range(1,n+1):
		f = f * i

	return f 





