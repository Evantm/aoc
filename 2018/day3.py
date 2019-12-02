# from collections import defaultdict
# from math import sqrt
# if __name__ == '__main__':
# 	# Point = namedtuple('Point',['x','y'])

# 	# Box = namedtuple('Box',['Point','width','height'])
# 	# box1 = Box(1,1,2,2)
# 	# print(box1.x2)
# 	def parser(line):
# 		line = line[:-1].replace('#','')
# 		id_,rest = line.split('@')
		
# 		left_top, size = rest.split(':')
# 		left,top = left_top.split(',')
# 		w,h = size.split('x')


# 		return int(id_), int(left), int(top), int(w), int(h)

# 	square_count = defaultdict(int)
# 	with open('day3.input') as file:
# 		for line in file:
# 			id_, left, top, width, height = parser(line)
# 			for square in range(left,left+width+1):
# 				for square2 in range(top,top+height+1):
# 					x_y = (f'{square},{square2}')
# 					square_count[x_y] += square_count[x_y] + 1 

# 		print(sqrt(sum([1 for k,v in square_count.items() if v > 1])))


import re
from collections import Counter

claims = [[*map(int, re.findall(r'\d+', l))] for l in open('day3.input') if l]
print(claims[0])
squares = lambda c: ((i, j) for i in range(c[1], c[1]+c[3])
                            for j in range(c[2], c[2]+c[4]))
fabric = Counter(s for c in claims for s in squares(c))

part1 = sum(1 for v in fabric.values() if v > 1)
part2 = next(c[0] for c in claims if all(fabric[s] == 1 for s in squares(c)))

print(part1)