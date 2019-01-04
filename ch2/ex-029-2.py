import sys

def cout(c):
	'''Print the single character 'c' to stdout.'''
	if len(c) != 1:
		raise Exception("cheater!")
	sys.stdout.write(c)

def pound2(count):
	pounds_in_a_row = 0

	while pounds_in_a_row < count:
		cout("#")
		pounds_in_a_row = pounds_in_a_row + 1
	cout("\n")

	# else :
		# def pound2(count):
		# '''A version of 'pound' using loops instead of string multiplication.'''
		# pounds_in_a_row = 0
		# while pounds_in_a_row < count:
		# 	cout("#")
		# 	pounds_in_a_row = pounds_in_a_row + 1


def solution(row):
	pound = pound2	
	row = row
	# if row < 5:

	while row < 5:
		pound(row)
		row = row + 1

	# else:		
	# when row >= 5 
	while row > 0:
		pound(row)
		row = row - 1	
	

solution(15)




