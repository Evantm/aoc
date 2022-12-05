input_ =  open("aoc2020_02").read()
count = 0

for line in input_.split('\n'):

	req, password = line.split(':')
	c = Counter(password)
	del c[' ']
	min_,max_ = req.split('-')
	max_,letter = max_.split(' ')
	if(c[letter] in [*range(int(min_),int(max_)+1)]):
		count += 1
print(count)
count = 0
for line in input_.split('\n'):

	req, password = line.split(':')
	min_,max_ = req.split('-')
	max_,letter = max_.split(' ')
	if (password[int(min_)] != password[int(max_)] and letter in [password[int(min_)],password[int(max_)]]):
		count+=1

print(count)