from collections import Counter, defaultdict
from copy import deepcopy
input_lines = open('07.input').read()

sample = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

dir_dict = { '!': 0 }
sum_1 = 0
current_dir = ['!']
for line in input_lines.split('\n'):
	if line.startswith('$ cd'):
		if line == '$ cd /': current_dir = ['!']
		elif line == '$ cd ..': current_dir = current_dir[:-1]  #this line was else which burned an hour I hate it
		else: current_dir.append(line.split(' ')[-1])
	elif line.startswith('$ ls'): pass
	else:
		if line.startswith('dir'): 
		#add to parent
			dir_dict[''.join(current_dir)+line.split(' ')[1]] = 0
		else:
			file_size = int(line.split(' ')[0])
			for i in range(len(current_dir)):
				dir_dict[''.join(current_dir[:i+1])] += file_size
sum_2 = 10**80 # hope this is big enough
smallest_needed = (30000000 - (70000000 - dir_dict['!'])) # free space
for k,v in dir_dict.items():
	# print(k,v)
	if v < 100000:
		sum_1 += v
	if v >= smallest_needed:
		sum_2 = min(sum_2,v)
print(sum_1)
print(sum_2)