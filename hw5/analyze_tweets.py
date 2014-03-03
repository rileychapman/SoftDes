

def unicode_to_string(uni):
	"""
	Converts a unicode string to a python string 
	uni: a unicode string 
	returns: a python string
	"""
	import unicodedata #used to convert unicode strings
	return unicodedata.normalize('NFKD',uni).encode('ascii','ignore')

def un_uni_list(l):
	"""
	Converts a list of unicode strings to a list of python strings 
	l:list of unicode strings
	returns: a list of python strings
	"""
	returnList = []
	for element in l:
		if type(element) == unicode:
			newElement = unicode_to_string(element)
			returnList.append(newElement)
		else: #to make sure unicode_to_string doesn't break
			print "Error in input: expected list of unicode strings"
	return returnList

def convert_to_LoL_words (L):
    """
    Takes in a list of tweets, makes each tweet into a list of lists of words,
    and takes out common, unimportant words. 
    
    L: List of tweets
    return_list: list of lists that contains the words in the tweets
    """
    import re    
    K=[]  # creates an empty list
    for element in L:
        list_words= re.findall (r'\w+', element)  #searches through the list for white space and divides the list into new lists wherever it finds the white space
        K.append (list_words)  #adds the element of the list to a bigger list, K
    return K
    
def make_lowercase (L):
    """
    Takes in a list of lists and makes one list of all the words lowercase.
    L=list of list of words
    K: list of lowercase words
    """
    
    K=[]   #generates an empty list K
    for item in L:
        for jitem in item:  #searches through each item of each item in the list
            x=jitem.lower()   #makes all the words lowercase
            K.append (x)  #adds the lowercase version to a new list, K
    return K
    
def word_frequencies (L):
    """
    Takes in a list of lowercase words and creates a dictionary indicating 
    how often that word appears in the list. 
    
    L: list of lowercase words
    d: dictionary mapping a word to the number of times it is found in the list
    """
    
    d={}  #creates an empty dictionary
    for element in L:  #goes through each element in L
        result=element in d   #checks to see if element is a key in dictionary d
        if result ==True:  
            d[element]+=1   #if it is in d, the value associated with that key gets increased by one
        else:
            d[element]=1   #if it is not in d, a new key is created for that word
    return d   #returns the dictionary
    
def word_counter (L):
    """
    Takes in a list of tweets and calculates the number of times each word appears
    L: list of tweets
    result: dictionary mapping a word to the number of times it is found in the list
    """
    words = convert_to_LoL_words (L)   #converts a list of tweets to a list of lists of words
    lowercase=make_lowercase (words)  #converts a list of lists of words into a list of lowercase words
    freq = word_frequencies (lowercase)  #creates a dictionary that indicates how often each word appears in the list
    return freq  #returns a dictionary mapping a word to the number of times it is found in the list. 

def make_to_string (d, scalar):
    """
    Takes in a dictionary with keys that are words (strings) and values that 
    are word frequencies (integers) and returns a string with the following format
    'word: number
    word: numner'
    
    d: dictionary mapping a word to the number of times it is found
    res_string: string in the above format
    """
    res_string = ''     #creates an empty string
    for element in (d):
        x= str(scalar*d[element])  #assigns a scaled version of the value at element  to variable x
        y=':'
        res_string = res_string + element + y + x +','  #creates a string that concatinates itself with the key, a colon, and the scaled value and then moves to thte next line
    return  res_string

def wordle_interface(d):
	"""
	links to wordle.net and creates a wordle using the frequencies dictionary
	"""
	from pattern.web import URL
	
	#url = URL(string='http://wordle.net/compose', method='GET', query={})
	#print url.open(timeout=10, proxy=None).read()

	#q = {"wordcounts":"here goes your text"}
	# OR
	q = {"wordcounts":'Riley:5,is:2,awesome:4'}
	
	url = URL(string="http://wordle.net/compose", query=q)
	thing = url.open(timeout=10, proxy=None).read()

	print url.parts

	return thing

	




