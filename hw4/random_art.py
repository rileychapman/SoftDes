# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: rileychapman and pruvolo 
"""

# you do not have to use these particular modules, but they may help
from random import randint
from math import pi
from math import sin
from math import cos
import uuid #for unique file names
import Image

def build_random_function(min_depth, max_depth):
	""" 
		Generates a nested fuction of the specified complexity

		min_depth: the miniumum amount of nesting for the generated function
		max_depth: the maximum amoint of nesting fot the generated function
		returns: a random nested function in nested list form 
	"""

	if max_depth == 0: # the base case, we have reached the maximum depth
		xory = randint(1,2)
		if xory == 1:
			return(['x'])
		elif xory == 2:
			return(['y'])

	if min_depth <= 0: # we are between the min and max depth, returning the base case is an option
		n = randint(1,7)
		if n == 1:
			return(['prod',build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)])
		elif n == 2:
			return(['cos_pi',build_random_function(min_depth-1,max_depth-1)])
		elif n == 3:
			return(['sin_pi',build_random_function(min_depth-1,max_depth-1)])
		elif n == 4:
			return(['cubed', build_random_function(min_depth-1,max_depth-1)])
		elif n == 5:
			return(['multi_sin',build_random_function(min_depth-1,max_depth-1)])
		elif n == 6:
			return(['x'])
		elif n == 7:
			return(['y'])

	
	else: # we are above the min depth, choose a function at random and continue 
		n = randint(1,5) 
		if n == 1:
			return(['prod',build_random_function(min_depth-1,max_depth-1),build_random_function(min_depth-1,max_depth-1)])
		elif n == 2:
			return(['cos_pi',build_random_function(min_depth-1,max_depth-1)])
		elif n == 3:
			return(['sin_pi',build_random_function(min_depth-1,max_depth-1)])
		elif n == 4:
			return(['cubed', build_random_function(min_depth-1,max_depth-1)])
		elif n == 5:
			return(['multi_sin',build_random_function(min_depth-1,max_depth-1)])
	

#if __name__ == '__main__':
	#print build_random_function(2,5)



def evaluate_random_function(f, x, y):
	""" 
		Evaluates a nested function in list form for the given values 

		f: the function to be evaluated in list form 
		x: value to plug in for x 
		y: value to plug in for y
		returns: a value for the fucntion at the specified x and y points
	"""

	if f[0] == 'prod': # check which function it is and perform the correct operation 
		result = evaluate_random_function(f[1],x,y) * evaluate_random_function(f[2],x,y)
	elif f[0] == 'sin_pi':
		result = sin(evaluate_random_function(f[1],x,y)*pi)
	elif f[0] == 'cos_pi':
		result = cos(evaluate_random_function(f[1],x,y)*pi)
	elif f[0] == 'cubed':
		result = evaluate_random_function(f[1],x,y)**3
	elif f[0] == 'multi_sin':
		result = sin(evaluate_random_function(f[1],x,y)*5)
	elif f[0] == 'x': # if we are at the base of the function, plug in the corect value 
		result = x 
	elif f[0] == 'y':
		result = y
	return(result)


#if __name__ == '__main__':
	#print evaluate_random_function(build_random_function(2,5),3,3)

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
	""" 
		Maps the input value that is in the interval [input_interval_start, input_interval_end]
		to the output interval [output_interval_start, output_interval_end].  The mapping
		is an affine one (i.e. output = input*c + b).
	
		val: the value to be mapped 
		input_interval_start: min of the input interval
		input_interval_end: max of the input interval
		output_interval_start: min of the output interval
		output_interval_end: max of the 
	"""
	inputRange = input_interval_end - input_interval_start
	outputRange = output_interval_end - output_interval_start
	mappedVal = (((val - input_interval_start)*outputRange)/inputRange)+output_interval_start
	return(mappedVal)

def build_picture():
	""" 
		Builds an image using randomly generated functions and the PIL 
	"""
	redFunc = build_random_function(2,5) #generate random functions for the three color channels of the picture
	greenFunc = build_random_function(3,7)
	blueFunc = build_random_function(4,5)

	sizex  = 600	#define the denesions of the picture
	sizey = 400
	im = Image.new("RGB", (sizex,sizey))
	pixels = im.load()

	for xpix in range(0,sizex-1):
		x = remap_interval(xpix,0.0,sizex-1,-1.0,1.0)
		for ypix in range(0,sizey-1):
			y = remap_interval(ypix,0.0,sizey-1,-1.0,1.0)

			red = evaluate_random_function(redFunc,x,y)
			green = evaluate_random_function(greenFunc,x,y)
			blue = evaluate_random_function(blueFunc,x,y)

			redScaled = int(remap_interval(red,-1.0,1.0,0,255))
			greenScaled = int(remap_interval(green,-1.0,1.0,0,255))
			blueScaled = int(remap_interval(blue,-1.0,1.0,0,255))

			pixels[xpix,ypix] = (redScaled,greenScaled,blueScaled)
	filename = uuid.uuid4()
	filename = str(filename) + '.png'
	im.save(filename)
	#im.show()

if __name__ == '__main__':
		build_picture()




