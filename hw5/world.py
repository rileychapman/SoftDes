from PIL import Image
from PIL import ImageDraw
from PIL import ImageFront

import numpy as np 



def make_wordcloud(d,width,height,margin):
	"""
	Build the worclound using the frequency of the words as the weight.
	d: dictinary of words an their frequencies
	width: width of image in pixels
	height: height of image in pixles
	margin: margin of image in pixels

	Structure borrowed from Andreas Christian Mueller's  word_cloud
	"""

	font_path = "/usr/share/fonts/truetype/droid/DroidSansMono.ttf"

	#sort the dictionary

	#create the image
	img_grey = Image.new("L", (width,height))
	draw = ImageDraw.Draw(img_grey)
	integral = np.zeros((height, width), dtype=np.uint32)
	np.zeros((height, width), dtype=np.uint32)
	font_sizes, positions, orientations = [], [], []

	#initialize font size as a large enough value
	font_size = 10000

	



