'''
New Driver's License

You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

Task 
Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

Input Format 
Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

Output Format 
You will output an integer of the number of minutes that it will take to get your license.

Sample Input
'Eric'
2
'Adam Caroline Rebecca Frank'

Sample Output 
40
'''
"""Calculates the time the given person will take to get his/her driving license,
if the license if given alphabetically and n agents can work simultaneously."""
def find_license_generation_time():
	"""Gets the data for the calculate_license_generation_time() function and calls it."""
	name = input("Enter your name: ")
	n_agents = input("Enter the number of agents: ")
	others = input("Enter the name of other people: ")
	return calculate_license_generation_time(name, n_agents, others)


def calculate_license_generation_time(name: str, n_agents: int, others: str, time_per_person: float =20):
	"""Calculates the license generation time based to the alphabetical order of the people present.

	Parameters
	==========
	name: str
		The name of the person of calculate the time for.

	n_agents: int
		Number of the agents working at the department.

	others: str
		Name of other people present at the department at the time.

	time_per_person: float
		Time taken by an agent to generate the license for a single person

	Returns
	=======
	time_taken
		The time that will be taken to get the license of the person of the name.
	"""
	people_list = others.split()
	people_list.append(name)
	people_list.sort()

	no_of_people_before = 0
	for people in people_list:
		if people == name:
			break
		no_of_people_before += 1
	return (no_of_people_before // n_agents + 1) * time_per_person



if __name__ == '__main__':
	print(calculate_license_generation_time("Eric", 2, "Adam Caroline Rebecca Frank"),"minutes")
