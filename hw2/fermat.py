def check_fermat(a,b,c,n):
	if n > 2:
		if a**n+b**n==c**n:
			print "Holy smokes, Fermnat was wrong!"
	else:
		print "No, that doesn't work"

def fermat():
	print "a:"
	a = int(raw_input())
	print "b:"
	b = int(raw_input())
	print "c:"
	c = int(raw_input())
	print "n:"
	n = int(raw_input())
	
	check_fermat(a,b,c,n)

