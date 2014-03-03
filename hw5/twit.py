from pattern.web import *

def get_data(seconds,subject):
	stream = Twitter().stream(subject)
	for i in range(seconds):
		time.sleep(2)
		stream.update(bytes = 1024)
		print 'in loop', i
	return stream


def tweets(stream):

	resultList = []
	for i in range(len(stream)):
		#print stream[i].text
		if stream[i].lanuage == '':
			resultList.append(stream[i].text)

	return(resultList)
 
