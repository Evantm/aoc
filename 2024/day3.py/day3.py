import re
test_input = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

with open('day3.input') as file:
	file_contents = file.read()



x = re.findall("mul\(\d+,\d+\)", file_contents)

a = 0
for i in x:
	i = i.replace('mul(','')
	i = i.replace(')','')
	x,y = i.split(',')
	a += (int(x) * int(y))
print(a)


test_input_2 = '''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'''
a = 0

input_ = file_contents
x2 = re.sub("don't\(\)[\s\S]+?(do\(\)|$)", "", input_)
x3 = re.findall("mul\(\d+,\d+\)", x2)
for i in x3:
	i = i.split('mul(')[1]
	i = i.replace('mul(','')
	i = i.replace(')','')
	x,y = i.split(',')
	a += (int(x) * int(y))
print(a)