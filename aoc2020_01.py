nums = []
with open("aoc2020_01.txt") as file:
	for line in file:
		nums.append(int(line))
one_pass = {}
for i in nums:
	one_pass[i] = 2020-i
twopass = {}
for i in one_pass.vals():
	twopass[i] = 2020-i

nums_s = set(nums)

if  
# for i in nums:
# 	for j in nums:
# 		for k in nums:
# 			if i + j + k == 2020:
# 				print(i*j*k)