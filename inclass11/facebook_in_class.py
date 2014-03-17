class User:
	pass

def print_user_information(u):
	print "User's name: " + u.name
	print "User's home town " + u.home_town
	print "Friends:"
	for friend in u.friends:
		print "      " + friend.name

def make_friends(user_1, user_2):
	user_1.friends.append(user_2)


if __name__ == '__main__':

	u = User()
	u.name = "Riley Chapman"
	u.home_town = "Ticonderoga, NY"
	u.friends = []

	u2 = User()
	u2.name = "Paul Ruvolo"
	u2.home_town = "Los Altos, CA"
	u2.friends = []

	make_friends(u,u2)

	print_user_information(u)

