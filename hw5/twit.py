

def get_data(times,subject):
	"""
	Pulls the latest tweet from twitter that contains a specified string, 
	and adds it to a list of tweets for a specified amount of times. 
	times: the number of times that twitter is checked
	subject: the string that is searched for in tweets
	returns: a list of all the information about all the tweets gathered
	"""
	from pattern.web import *
	stream = Twitter().stream(subject) #setup twitter stream
	for i in range(times):
		time.sleep(2)
		stream.update(bytes = 1024)
		print 'in loop', i #to make sure the code is running
	tweets = tweets(stream) #return all the data gathered
	return tweets


def tweets(stream):
	"""
	Takes all the raw data from twitter and pulls out just the tweets that
	do not have a specified language other than english. 
	stream: list of tweet data
	returns: list of tweets
	"""
	resultList = []
	for i in range(len(stream)):
		#print stream[i].text
		if stream[i].lanuage == '': #filtering out languages that are specified as other than english 
			resultList.append(stream[i].text)

	return(resultList)

if __name__ == '__main__':
	data = get_data(10,'Miley Cyrus')
	print tweets
