import time

input_lines = open('06.input').read()

sample = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

past_four = []
old = time.time()
for i,character in enumerate(input_lines):
	past_four.append(character)
	if len(past_four) >4: past_four = past_four[1:]
	if len(set(past_four)) == 4: 
		print("Part 1",i+1)
		break
print("Part One Time ", (time.time() - old)*1000,"ms")

old = time.time()
for i,character in enumerate(input_lines):
	# print(i,character)
	past_four.append(character)
	if len(past_four) >14: past_four = past_four[1:]
	if len(set(past_four)) == 14: 
		print("Part 2",i+1)
		break

print("Part Two Time ", (time.time() - old)*1000,"ms")
