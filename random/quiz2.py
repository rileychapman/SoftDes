def sum_of_squares(n):
	sum = 0
	for i in range(1,n+1):
		sum = sum + (i * i)
	return sum 

def filter_out_negative_numbers(L):
	newL = []
	for number in L:
		if number >= 0:
			newL.append(number)
	return newL