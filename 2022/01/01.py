maxes = []
inputs = open('01.input')
inputs = inputs.read()
elfs = (inputs.split('\n\n'))
for elf in elfs:
	sum_ = 0
	for val in (elf.split('\n')):
		if val != '': sum_ += int(val)
	maxes.append(sum_)
print(max(maxes))
print(sum(sorted(maxes)[-3:]))