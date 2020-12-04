file = open("aoc_2020_03.txt","r")

lines = file.read().split()
import fileinput
from math import prod

f = []

for line in lines:
    line = line.strip()
    f.append(line)
    width = len(line)

treenums = []

for r in [1, 3, 5, 7]:
    pos = -r
    trees = 0
    for line in f:
        pos = (pos + r) % width
        if line[pos] == '#':
            trees += 1
    treenums.append(trees)

pos = -1
trees = 0
for line in f[::2]:
    pos = (pos + 1) % width
    if line[pos] == '#':
        trees += 1
treenums.append(trees)
print(treenums)
input_ = '''..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#'''



    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.

grid = input_.split()
grid = lines

x,y = 1,3
from collections import Counter
l = [] 
for _ in range(len(grid)):
	if x == len(grid):
		break
	# print(grid[x][y%len(grid[x])])
	l.append(grid[x][y%len(grid[x])])
	x += 1
	y += 3

print(Counter(l)['#'])


x,y = 1,1
from collections import Counter
l = [] 
for _ in range(len(grid)):
	if x == len(grid):
		break
	# print(grid[x][y%len(grid[x])])
	l.append(grid[x][y%len(grid[x])])
	x += 1
	y += 1

print(Counter(l)['#'])

x,y = 1,5
from collections import Counter
l = [] 
for _ in range(len(grid)):
	if x == len(grid):
		break
	# print(grid[x][y%len(grid[x])])
	l.append(grid[x][y%len(grid[x])])
	x += 1
	y += 5

print(Counter(l)['#'])
x,y = 1,7
from collections import Counter
l = [] 
for _ in range(len(grid)):
	if x == len(grid):
		break
	# print(grid[x][y%len(grid[x])])
	l.append(grid[x][y%len(grid[x])])
	x += 1
	y += 7

print(Counter(l)['#'])


x,y = 2,1
from collections import Counter
l = [] 
for _ in [*range(len(grid))][::2]:
	l.append(grid[x%len(grid)][y%len(grid[x%len(grid)])])
	y += 1
	x += 2
	if y == len(grid):
		break
print(Counter(l)['#'])