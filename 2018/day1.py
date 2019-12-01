
def part_one():
	with open("day1.input") as file:
		initial = 0
		for number in file:
			if '-' in number:
				# print("negative",number[1:])
				initial -= int(number[1:])
			if '+' in number:
				# print("positive",number[1:]) 
				initial += int(number[1:])
		print(initial)

def part_two():
	from collections import Counter
	counts = []
	numbers = []
	freq = 0
	with open("day1.input") as file:
		for number in file:
			if '-' in number:
				number = number[1:]
				numbers.append(-int(number))
			if '+' in number:
				number = number[1:]
				numbers.append(int(number))
	while True:
		for number in numbers:
			freq += number
			if freq in counts:
				print(freq)
				break #supper inefiecient
			counts.append(freq)
			# print(freq)

if __name__ == '__main__':
	part_two()