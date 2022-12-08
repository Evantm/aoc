from copy import deepcopy
input_lines = open('08.input').read()

sample = '''30373
25512
65332
33549
35390'''
# sample = '''88788
# 87878
# 87778
# 87778
# 88888'''

# sum_1 = 0
# grid = []
# for line in sample.split('\n'):
# 	tree_line = []
# 	for tree in line:
# 		tree_line.append(int(tree))
# 	grid.append(tree_line)

# for i in grid:
# 	print(i)
# rot_90 = list(zip(*grid[::-1]))
# rot_90 = list(zip(*grid[::-1]))

# visible_grid = []
# visible = 0
# for i,tree_line in enumerate(grid):
# 	compare_tree = -1
# 	visible_tree_line = []
# 	for j,tree in enumerate(tree_line):
# 		is_edge = i == 0 or j == 0 or i == len(grid) - 1 or j == len(tree_line) - 1
# 		visible_tree_line.append([tree > compare_tree or is_edge, tree])
# 		# if i == len(grid) - 1:
# 		# 	print(tree)
# 		# print(visible_tree_line)
# 		compare_tree = max(tree,compare_tree)
# 	visible_grid.append(visible_tree_line)

# visible_grid_back = []
# for i,tree_line in enumerate(visible_grid):
# 	compare_tree = -1
# 	visible_tree_line = []
# 	for j,tree in enumerate(tree_line[::-1]):
# 		is_edge = i == 0 or j == 0 or i == len(grid) - 1 or j == len(tree_line) - 1
# 		visible_tree_line.append([tree[1] > compare_tree or is_edge or tree[0], tree[1]])
# 		# if i == 0:
# 		# 	print(tree)
# 		# print(visible_tree_line)
# 		compare_tree = max(tree[1],compare_tree)
# 	visible_grid_back.append(visible_tree_line[::-1])

# visible_grid_up = []
# for i,tree_line in enumerate(rot_90):
# 	compare_tree = -1
# 	visible_tree_line = []
# 	for j,tree in enumerate(tree_line):
# 		is_edge = i == 0 or j == 0 or i == len(grid) - 1 or j == len(tree_line) - 1
# 		visible_tree_line.append([tree > compare_tree or is_edge, tree])
# 		compare_tree = max(tree,compare_tree)
# 	visible_grid_up.append(visible_tree_line)

# visible_grid_up = list(zip(*visible_grid_up[::-1])) #180
# visible_grid_up = list(zip(*visible_grid_up[::-1])) #270

# grid_down = deepcopy(visible_grid_up)
# visible_grid_down = []
# for i,tree_line in enumerate(grid_down):
# 	compare_tree = -1
# 	visible_tree_line = []
# 	for j,tree in enumerate(tree_line):
# 		is_edge = i == 0 or j == 0 or i == len(grid) - 1 or j == len(tree_line) - 1
# 		visible_tree_line.append([tree[1] > compare_tree or is_edge, tree[1]])
# 		compare_tree = max(tree[1],compare_tree)
# 	visible_grid_down.append(visible_tree_line)

# visible_grid_down = list(zip(*visible_grid_down[::-1])) #360

# visible_grid_up = list(zip(*visible_grid_up[::-1])) #360


# for i,j,i2,j2 in zip(visible_grid,visible_grid_back,visible_grid_up,visible_grid_down):
# 	for k,l,k2,l2  in zip(i,j,i2,j2):
# 		print([k[0] or l[0] or k2[0] or l2[0], k[1]],end=' ')
# 		if k[0] or l[0] or k2[0] or l2[0]: visible += 1
# 	print()
# print(visible)

sample = '''30373
25512
65332
33549
35390'''
grid = []
for line in input_lines.split('\n'):
	tree_line = []
	for tree in line:
		tree_line.append(int(tree))
	grid.append(tree_line)



score_matrix = deepcopy(grid)
for i, tree_line in enumerate(grid):
	for j, tree in enumerate(tree_line):	
		score = 1
		seen = 0
		for i2 in range(i-1, -1, -1):
			seen += 1
			previous_tree = grid[i2][j]
			if previous_tree >= tree:
					break

		score *= seen
		seen = 0

		for j2 in range(j+1, len(tree_line)):
			seen += 1
			previous_tree = grid[i][j2]
			if previous_tree >= tree:
					break

		score *= seen
		seen = 0

		for i2 in range(i+1, len(tree_line)):
			seen += 1
			previous_tree = grid[i2][j]
			if previous_tree >= tree:
					break

		score *= seen
		seen = 0

		for j2 in range(j-1, -1, -1):
			seen += 1
			previous_tree = grid[i][j2]
			if previous_tree >= tree:
					break

		score *= seen

		score_matrix[i][j] = score
		
print(max([max(i) for i in score_matrix]))