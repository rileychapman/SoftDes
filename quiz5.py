""" 
Software Design
Quiz 5

author: Riley Chapman
instructor: Paul Ruvolo

"""

class Person:
	""" Represents a person with name and DOB attributes """
	def __init__(self,name,date_of_birth):
		self.name = name
		self.date_of_birth = date_of_birth

class Employee(Person):
	""" Represens an Employee that can tell if it earns more than a certain amount """
	def __init__(self,name,date_of_birth,date_of_hire,salary):
		self.name = name
		self.date_of_birth = date_of_birth
		self.date_of_hire = date_of_hire
		self.salary = salary

	def earn_more_than(self,level):
		""" Returns True if the employee earns more than the specified 
			level and False otherwise 

			level: the amount of money we are comparing the salary to 
			returns: True or False
		"""

		if self.salary > level:
			return True
		else:
			return False

class Manager(Employee):
	""" Represents a special Employee which keeps track of a list of other employees which
		report to it  
	"""

	def __init__(self,name,date_of_birth,date_of_hire,salary):
		self.name = name
		self.date_of_birth = date_of_birth
		self.date_of_hire = date_of_hire
		self.salary = salary
		self.direct_reports = []

	def add_direct_report(self,new_report):
		""" Adds the specefied employee as a direct report of the Manager
			new_report: Employee to add the the list of direct reports
		"""
		self.direct_reports.append(new_report)





