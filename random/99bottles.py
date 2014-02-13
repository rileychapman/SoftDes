def bottles(n):
	if n >= 1:
		print str(n) + " bottles of beer on the the wall, " + str(n) +  " bottles of beer. Take one down, pass it around, " + str(n-1) + " bottles of beer on the wall!"
		bottles(n-1)

