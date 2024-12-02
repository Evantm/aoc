

test_input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

with open('day2.input') as file:
	file_contents = file.read()

# count = 0
def is_safe(numbers) -> bool:

	decreasing = True
	increasing = True
	safe = True
	
	for i,number in enumerate(numbers[1:]):
		# print(i,number,numbers[i])
		number = int(number)
		last_number = int(numbers[i])

		decreasing = decreasing & (number < last_number)
		increasing = increasing & (number > last_number)
		if abs(int(numbers[i]) - int(number)) > 3:
			safe = False

	return (increasing and safe) or (decreasing and safe)

for line in file_contents.split('\n'):
	# print(line.split())
	numbers = line.split()

	# print(numbers)
	decreasing = True
	increasing = True
	safe = True
	for i,number in enumerate(numbers[1:]):
		# print(i,number,numbers[i])
		number = int(number)
		last_number = int(numbers[i])
		decreasing = decreasing & (number < last_number)
		increasing = increasing & (number > last_number)
		if abs(int(numbers[i]) - int(number)) > 3:
			safe = False

	if (increasing and safe) or (decreasing and safe):
		count += 1
print(count) 

count = 0
for line in file_contents.split('\n'):
	numbers = line.split()
	all_safe = False
	all_safe = all_safe or is_safe(numbers)
	for i in range(len(numbers)):
		short_list = numbers[:i]+numbers[i+1:]
		all_safe = all_safe or is_safe(short_list)
	print(all_safe)
	if all_safe: count += 1
print(count)