import sys

def oracle(input):
	'''A cheater solution to help testing non-cheater solutions.'''
	def maybe_double(i,d):
		'''Double the digit iff it's in an even position.'''
		if i % 2 == 0:
			return double(d)
		else:
			return d
	checksum = sum(maybe_double(i+1,int(c)) 
		for (i,c) in enumerate(reversed(input)))
	return checksum % 10 == 0

def test():
	for number in range(100000):
		input = str(number)
		if oracle(input) != solution(input):
			print "The 'solution()' is wrong for input '%s'!" % input
			return
	print "All tests passed!"

def double(d):
	'''Double a digit and
	add the digits of the result together.
	'''
	if d * 2 >= 10:
		return ((d * 2) - 10) + 1
	else:
		return d * 2 

def solution(input):
	# Answer when the input has even length
	answer_even_length = 0
	answer_odd_length = 0
	count = 0
	position = 'even'

	for c in input:
		count = count + 1
		d = int(c)
		if position == 'odd':
			answer_even_length = answer_even_length + d
			answer_odd_length = answer_odd_length + double(d)
			position = "even"
		else:
			answer_even_length = answer_even_length + double(d)
			answer_odd_length = answer_odd_length + d
			position = 'odd'
	print answer_even_length

	even_length = (count % 2) == 0
	if even_length:
	# The checksum is good if it's divible by 10.
		return (answer_even_length % 10) == 0
	else:
		return (answer_odd_length % 10) == 0

def main():
	input = raw_input("Enter a number: ") # sys.stdin.readline()
	solution(input)

if __name__ == '__main__':
	main()