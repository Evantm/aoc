from collections import Counter
input_lines = open('05.input').read()
# [F]         [L]     [M]            
# [T]     [H] [V] [G] [V]            
# [N]     [T] [D] [R] [N]     [D]    
# [Z]     [B] [C] [P] [B] [R] [Z]    
# [M]     [J] [N] [M] [F] [M] [V] [H]
# [G] [J] [L] [J] [S] [C] [G] [M] [F]
# [H] [W] [V] [P] [W] [H] [H] [N] [N]
# [J] [V] [G] [B] [F] [G] [D] [H] [G]
#  1   2   3   4   5   6   7   8   9 

sample = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''

stacks = [['F','T','N','Z','M','G','H','J'],['J','W','V'],['H','T','B','J','L','V','G'],['L','V','D','C','N','J','P','B'],['G','R','P','M','S','W','F'],['M','V','N','B','F','C','H','G'],['R','M','G','H','D'],['D','Z','V','M','N','H'],['H','F','N','G']]


steps = input_lines.split('\n\n')[1]

# for line in steps.split('\n'):
# 	count_stack, from_stack, to_stack = int(line.split(' ')[1]), int(line.split(' ')[3]),int(line.split(' ')[-1])
# 	# print(count_stack,from_stack,to_stack,line)
# 	for i in range(count_stack):
# 		# print(stacks[from_stack-1],stacks[to_stack-1])
# 		stacks[to_stack-1].insert(0,stacks[from_stack-1][0])
# 		stacks[from_stack-1] = stacks[from_stack-1][1:]

# 		# print(stacks[from_stack-1],stacks[to_stack-1])
# 		# print()

# for i in stacks:
# 	print(i[0],end='')

# stacks = [['N','Z'],['D','C','M'],['P']]
# steps = sample.split('\n\n')[1]

for line in steps.split('\n'):
	count_stack, from_stack, to_stack = int(line.split(' ')[1]), int(line.split(' ')[3]),int(line.split(' ')[-1])
	print(count_stack,from_stack,to_stack,line)
	print(stacks[to_stack-1])
	temp_stack = stacks[from_stack-1][0:0+count_stack]
	temp_stack.extend(stacks[to_stack-1])
	stacks[from_stack-1] = stacks[from_stack-1][count_stack:]
	stacks[to_stack-1] = temp_stack
	print(stacks[to_stack-1])
	print(stacks)
for i in stacks:
	print(i[0],end='')
print()