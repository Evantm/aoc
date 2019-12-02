from math import floor

def part_one():

	# print(sum([*map(lambda a : a//3 - 2,[int(i) for i in open('day1.input')])]))


	a = lambda a: a//3-2

	with open('day1.input') as file:
		b = [a(int(i)) for i in file]
		print(sum(b))


def part_two():

	
	a = lambda a: floor(a/3)-2
	all_sum = 0

	with open('day1.input') as file:
		for i in file:
			t = a(int(i))
			sum_ = t
			while a(int(t)) > 0:
				t = a(int(t))
				sum_ += t
			all_sum += sum_
		print(all_sum)

if __name__ == '__main__':
	part_one()
	part_two()