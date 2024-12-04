example_input = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

with open('day4.input') as file:
	file_contents = file.read()


count = 0

horizontal = 0
backwards = 0 

vertical_up = 0
vertical_down = 0

diagonal_right = 0
diagonal_left = 0


original_grid = file_contents.split('\n')
rotated_nintey = list(zip(*original_grid[::-1]))

for i,line in enumerate(original_grid):
	horizontal += line.count('XMAS')
	backwards += line.count('SAMX')
	for j,char in enumerate(line):
		try:
			diagonal_right_str = original_grid[i][j]+original_grid[i+1][j+1]+original_grid[i+2][j+2]+original_grid[i+3][j+3]
			if diagonal_right_str == 'XMAS' or diagonal_right_str == 'SAMX': 
				diagonal_right += 1
		except Exception as e:
			pass

for i,line in enumerate(rotated_nintey):
	line = ''.join(list(line))
	vertical_up += line.count('XMAS')
	vertical_down += line.count('SAMX')
	for j,char in enumerate(line):
		try:
			diagonal_left_str = rotated_nintey[i][j]+rotated_nintey[i+1][j+1]+rotated_nintey[i+2][j+2]+rotated_nintey[i+3][j+3]
			if diagonal_left_str == 'XMAS' or diagonal_left_str == 'SAMX': 
				diagonal_left += 1
		except Exception as e:
			pass

print(horizontal+backwards+vertical_up+vertical_down+diagonal_right+diagonal_left)
