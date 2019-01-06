import sys

def cout(c):
	'''Print the single character 'c' to stdout.'''
	if len(c) != 1:
		raise Exception("cheater!")
	sys.stdout.write(c)

def print_pound(count):
	pounds_in_a_row = 0

	while pounds_in_a_row < count:
		cout("#")
		pounds_in_a_row = pounds_in_a_row + 1
	cout("\n")

def solution(width):
	pound = print_pound	
	row = 1

	while row < width:
		pound(row)
		row = row + 1

	while row > 0:
		pound(row)
		row = row - 1	
	
solution(15)




