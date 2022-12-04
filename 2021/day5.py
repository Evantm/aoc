from collections import Counter
# input_lines = open('04.input').read()

sample = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''


sum_1 = 0
pts = []
for line in sample.split('\n'):
	first_pair,second_pair = line.split(' -> ')
	first_start, first_end = first_pair.split(',')
	second_start, second_end = second_pair.split(',')

	first_start = int(first_start)
	second_start = int(second_start)

	first_end = int(first_end)
	second_end = int(second_end)


	start_diff = abs(first_start - second_start)
	end_diff = abs(first_end - second_end)


	if first_start==second_start or first_end==second_end: #vert or hor alligned
		for x in range(min(first_start,second_start),max(first_start,second_start)+1):
			for y in range(min(first_end,second_end),max(first_end,second_end)+1):
				pts.append((x,y))
print(pts)
print(([x for (x,y) in Counter(pts).items() if y>1]))
print(sum_1)




# sum_2 = 0
# for line in sample.split('\n'):
# 	...
# 	