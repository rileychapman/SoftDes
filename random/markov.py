def text_to_dictionary(file):
	"""
	file: name of a text file to analyze
	returns: dictionary with prefixes as keys and lists of suffixes as elements
	"""
	import re #for whitespace division
	d ={}
	fp = open(file)
	text =  fp.read()
	list_words= re.findall (r'\w+', text) 
	list_words = make_lowercase_list(list_words)
	max_prefix_length = 10 #number of words
	for prefix_length in range(1,max_prefix_length+1): 
		for i in range(len(list_words)-2*prefix_length):
			j = 0
			prefix = ''
			suffix = ''
			while j < prefix_length:
				if j == prefix_length - 1:
					prefix = prefix + list_words[i+j]
					suffix = suffix + list_words[i+prefix_length+j]
				else:
					prefix = prefix + list_words[i+j] + ' '
					suffix = suffix + list_words[i+prefix_length+j] + ' '
				j += 1
			if prefix in d:
				d[prefix].append(suffix)
			else:
				d[prefix] = [suffix]


	#d = {'hi': ['hello'], 'hello there': ['how are you'], 'hey': ['hey', 'hi', 'hello']}
	return d


def response(d):
	"""
	uses the dictionary of prefixes and suffixes to generate a response to raw input 
	"""
	from random import randint

	to_end = 0
	while to_end == 0:
		input = raw_input('~ ')
		input = make_lowercase_string(input)
		if input == 'quit' or input == 'end' or input == 'q':
			to_end = 1
			print 'quitting'

		elif input in d: 
				number_of_responses = len(d[input])
				choice = randint(0,number_of_responses-1)
				response = d[input][choice]
				print "     "+response
		else:
			print ''

def make_lowercase_string (s):
	"""
	Takes in a string and makes all the characters lowercase
	s: a string
	returns: an entirely lowecase string
	"""
	
	K=''  #generates an empty list K
	for item in s:
		for jitem in item:  #searches through each item of each item in the list
			x=jitem.lower()   #makes all the words lowercase
			K += x  #adds the lowercase version to a new list, K
	return K

def make_lowercase_list (L):
	"""
	Takes in a list and makes one list of all the words lowercase.
	L=list of list of words
	K: list of lowercase words
	"""
	
	return_list=[]   #generates an empty list K
	for item in L:  #searches through each item of each item in the list
		x=item.lower()   #makes all the words lowercase
		return_list.append(x)  #adds the lowercase version to a new list, K
	return return_list

if __name__ == '__main__':
	d = text_to_dictionary('lesMis.txt')
	#d = text_to_dictionary('testtext.txt')
	response(d)
