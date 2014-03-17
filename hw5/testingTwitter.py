from pattern.web import *

def trending():
	print Twitter().trends()

def hash(hashtag):
	s = Twitter().stream(hashtag)
	for i in range(10):
		time.sleep(1)
		s.update(bytes = 1024)
		print s



