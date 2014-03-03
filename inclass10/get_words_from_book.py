
def get_words_from_book(book_name):
	book = open(book_name, 'r')
	book = book[book.index(" ***")+4:]
	book = book[:book.index('End of the Project Gutenberg EBook')]

#to get a list of words
#re.findall("[a-zA-Z]+",name_of_book)
#or
#re.findall("\w",name_of_book)


