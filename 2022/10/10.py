
input_lines = open('10.input').read()

sample = '''noop
addx 3
addx -5'''


cycle_count = 0
x_addr = 1
for cycle, line in enumerate(sample.split('\n')):
	cycle_count += 1
	if line == 'noop': continue
	val = line.split(' ')[1]
	cycle_count += 1
	x_addr += int(val)
	print(cycle_count,x_addr)