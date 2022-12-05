from collections import Counter
input_lines = open('05.input').read()

stacks = [['F','T','N','Z','M','G','H','J'],['J','W','V'],['H','T','B','J','L','V','G'],['L','V','D','C','N','J','P','B'],['G','R','P','M','S','W','F'],['M','V','N','B','F','C','H','G'],['R','M','G','H','D'],['D','Z','V','M','N','H'],['H','F','N','G']]


steps = input_lines.split('\n\n')[1]

# for line in steps.split('\n'):
# 	count_stack, from_stack, to_stack = int(line.split(' ')[1]), int(line.split(' ')[3]),int(line.split(' ')[-1])

# 	for i in range(count_stack):

# 		stacks[to_stack-1].insert(0,stacks[from_stack-1][0])
# 		stacks[from_stack-1] = stacks[from_stack-1][1:]

# for i in stacks:
# 	print(i[0],end='')

for line in steps.split('\n'):
	count_stack, from_stack, to_stack = int(line.split(' ')[1]), int(line.split(' ')[3]),int(line.split(' ')[-1])

	temp_stack = stacks[from_stack-1][0:0+count_stack]
	temp_stack.extend(stacks[to_stack-1])
	stacks[from_stack-1] = stacks[from_stack-1][count_stack:]
	stacks[to_stack-1] = temp_stack


for i in stacks:
	print(i[0],end='')
	
print()