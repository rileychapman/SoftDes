def sumNumbers(n):
	if n <= 0:
		return 0 
	return sumNumbers(n-1) + n 

def factorial(n):
	if n <= 1:
		return 1
	return factorial(n-1) * n

def fib(n):
	if n == 0:
		print '1'
		return 1

	elif n == 1:
		print'1'
		return 1
	else:
		value  = fib(n-1) + fib(n-2) 
		print value
		return fib(n-1) + fib(n-2)

	
	
