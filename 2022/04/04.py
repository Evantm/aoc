
input_lines = open('04.input').read()

sample = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


sum_1 = 0
for line in input_lines.split('\n'):
	first_pair,second_pair = line.split(',')
	first_start, first_end = first_pair.split('-')
	second_start, second_end = second_pair.split('-')

	first_start = int(first_start)
	second_start = int(second_start)

	first_end = int(first_end)
	second_end = int(second_end)
	if first_start <= second_start and first_end >= second_end:
		sum_1 += 1
	elif second_start <= first_start and second_end >= first_end:
		sum_1 +=1 
print(sum_1)

sum_2 = 0
for line in input_lines.split('\n'):
	first_pair,second_pair = line.split(',')
	first_start, first_end = first_pair.split('-')
	second_start, second_end = second_pair.split('-')

	first_start = int(first_start)
	second_start = int(second_start)

	first_end = int(first_end)
	second_end = int(second_end)

	first_range = list(range(first_start,first_end+1))
	second_range = list(range(second_start,second_end+1))

	if  (len(set(first_range).intersection(set(second_range)))) > 0:
		sum_2 += 1

print(sum_2)
