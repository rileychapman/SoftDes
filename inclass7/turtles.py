from swampy.TurtleWorld import *
from math import pi 

def my_square(x,y,s):
	""" Takes the coordinates of the oweer left hand corner of a square and 
		the lenght of the side of the square, then draws the square

		x: x coordinate of lower left hand corner
		y: y coordinate of lower left hand corner
		s: length of the side of the square
	"""

	
	world = TurtleWorld()
	bob = Turtle()
	bob.x = x
	bob.y = y
	bob.heading = 0
	fd(bob,s) 
	lt(bob)
	fd(bob,s)
	lt(bob)
	fd(bob,s)
	lt(bob)
	fd(bob,s)

def my_regular_polygon(x,y,s,sides):
	""" x: x coordinate of lower left hand corner
		y: y coordinate of lower left hand corner
		s: length of the side of the square
		sides: number of sides
	"""
	world = TurtleWorld()
	bob = Turtle()
	bob.x = x
	bob.y = y
	bob.heading = 0
	bob.delay = .0001
	for n in range(0,sides):
		fd(bob,s)
		lt(bob,360.0/sides)



def my_circle(x,y,radius):
	""" x: x coordinate of bottom
		y: y coordinate of bottom
		radius: radius of the circle
	"""
	n = int(.3*2*radius)
	s = 2*pi*radius/n

	my_regular_polygon(x,y,s,n)

def snow_flake_side(turtle,l,level):
	""" Draw a side of the snowflake curve with side length l and recursion depth of level """

	if level == 1:
		fd(turtle,l)
		rt(turtle,60)
		fd(turtle,l)
		lt(turtle,2*60)
		fd(turtle,l)
		rt(turtle,60)
		fd(turtle,l)
	else:
		snow_flake_side(turtle,l/3,level-1)
		rt(turtle,60)
		snow_flake_side(turtle,l/3,level-1)
		lt(turtle,2*60)
		snow_flake_side(turtle,l/3,level-1)
		rt(turtle,60)
		snow_flake_side(turtle,l/3,level-1)

	   

def full_snow_flake(turtle,l,level):
	
	snow_flake_side(bob,l,level)
	lt(bob,120)
	snow_flake_side(bob,l,level)
	lt(bob,120)
	snow_flake_side(bob,l,level)


if __name__ == '__main__':
	#my_regular_polygon(-100,-100,100,100)
	#my_circle(0,-100,100)
	world = TurtleWorld()
	bob = Turtle()
	bob.delay = .001
	bob.y = -200
	full_snow_flake(bob,100,5)
	wait_for_user()
