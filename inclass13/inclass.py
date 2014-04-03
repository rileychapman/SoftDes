import math

def ack(m,n):
	""" Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
	if m == 0:
		return n+1
	elif m > 0 and n == 0:
		return ack(m-1,1)
	elif m > 0 and n > 0:
		return ack(m-1,ack(m,n-1))

def estimate_pi():
	k = 0
	summation = 1e-15
	total = 0
	while summation >= 1e-15:
		summation = (math.factorial(4*k) * (1103 + 26390* k))/(math.factorial(k)^4 * 396^(4*k))
		total += summation
		k += 1

	pi_inv = (2*math.sqrt(2)*total)/9801
	#pi = 1/pi_inv
	return total


