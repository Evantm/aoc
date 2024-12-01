from itertools import zip_longest as zl
input_lines = open('13.input').read()

sample = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

def check2(left,right):
	if isinstance(left,int) and isinstance(right,int):
		return (left > right) - (left < right) # True,False Bad. Any else good
	if isinstance(left,int) and isinstance(right,list): return check2([left],right)
	if isinstance(left,list) and isinstance(right,int): return check2(left,[right])
	if isinstance(left,list) and isinstance(right,list):
		for i in map(check2,left,right):
			print(i)
			if i: return i
		return check2(len(left),len(right)) #run out

sum_1 = 0
for i, line in enumerate(sample.split('\n\n')):
	print()
	print(f'Part {i+1}')

	left, right = line.split('\n')
	left, right = eval(left), eval(right)
	correct_order = check2(left,right)  == -1
	# print(correct_order)
	if correct_order:
		sum_1 += (i+1)
	print('#',i+1,correct_order)
	# print(i+1,check(left,right))
print(sum_1)
print(len(input_lines.split('\n\n')))

# 5185