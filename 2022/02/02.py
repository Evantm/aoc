

input_lines = open('02.input').read()

sample = '''A Y
B X
C Z'''
score = 0
for line in input_lines.split('\n'):
	first, second = line.split(' ')
	if second == 'X':
		score += 1
		if first == 'A': score += 3
		if first == 'B': score += 0
		if first == 'C': score += 6
	if second == 'Y':
		score += 2
		if first == 'A': score += 6
		if first == 'B': score += 3
		if first == 'C': score += 0
	if second == 'Z':
		score += 3
		if first == 'A': score += 0
		if first == 'B': score += 6
		if first == 'C': score += 3
print(score)
score = 0
for line in input_lines.split('\n'):
	first, second = line.split(' ')
	if second == 'X': #win
		score += 0 #win
		if first == 'A': score += 3
		if first == 'B': score += 1
		if first == 'C': score += 2
	if second == 'Y': #draw
		score += 3
		if first == 'A': score += 1
		if first == 'B': score += 2
		if first == 'C': score += 3
	if second == 'Z': # lose
		score += 6 
		if first == 'A': score += 2
		if first == 'B': score += 3
		if first == 'C': score += 1
print(score)