
input_lines = open('06.input').read()

sample = '''mjqjpqmgbljsphdztnvjfqwrcgsmlb'''

past_four = []

for i,character in enumerate(input_lines):
	# print(i,character)
	past_four.append(character)
	if len(past_four) >4: past_four = past_four[1:]
	if len(set(past_four)) == 4: 
		print(i+1)
		break
	# print(past_four)
for i,character in enumerate(input_lines):
	# print(i,character)
	past_four.append(character)
	if len(past_four) >14: past_four = past_four[1:]
	if len(set(past_four)) == 14: 
		print(i+1)
		break
	# print(past_four)