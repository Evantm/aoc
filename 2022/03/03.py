 
sample = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
sum_ = 0


input_lines = open('03.input').read()

for line in input_lines.split('\n'):
	midpoint = len(line) //2
	# print(line[:midpoint],line[midpoint:])
	first_half = line[:midpoint]
	second_half = line[midpoint:]
	commmon = list(set(first_half).intersection(set(second_half)))[0]
	if commmon.isupper(): sum_ += ord(commmon)-38
	elif commmon.islower(): sum_ += ord(commmon)-96
print(sum_)

sum_2 = 0
input_lines_list = input_lines.split('\n')
print(len(input_lines_list))
for line_index in range(0,len(input_lines_list),3):
	# print(line_index,line_index+1,line_index+2)
	# print(input_lines_list[line_index],input_lines_list[line_index+1],input_lines_list[line_index+2])
	common = list(set(input_lines_list[line_index]).intersection(set(input_lines_list[line_index+1])).intersection(set(input_lines_list[line_index+2])))[0]
	print(common)
	if common.isupper(): sum_2 += ord(common)-38
	elif common.islower(): sum_2 += ord(common)-96
print(sum_2)
