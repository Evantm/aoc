
file_contents = ''
with open('day1.input') as file:
	file_contents = file.read()
# print(file_contents)

list_one = []
list_two = []
for line in file_contents.split('\n'):
	if line:
		# print(line.split('   '))
		a,b = line.split('   ')
		list_one.append(int(a))
		list_two.append(int(b))


# print(list_one)
# print(list_two)

# run_sum = 0 
# for i,j in zip(sorted(list_one),sorted(list_two)):
# 	# print(i,j)
# 	# print(abs(i-j))
# 	run_sum += abs(i-j)
# print(run_sum)

run_sum_two = 0
from collections import Counter
c = Counter(list_two)
for i in list_one:
	# print(i*c[i])
	run_sum_two += (i*c[i])

print(run_sum_two)