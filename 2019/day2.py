
def part_one():
	with open('day2.input') as file:
		nums = eval(file.read())
		nums = list(nums)

		nums[1] = 12
		nums[2] = 2
		for i in range(0,len(nums),4):
			# print(nums[i])

			opcode = nums[i]

			if opcode == 1: #addiition
				nums[nums[i+3]] = nums[nums[i+2]] + nums[nums[i+1]]

			if opcode == 2: 
				nums[nums[i+3]] = nums[nums[i+2]] * nums[nums[i+1]]

			if opcode == 99:
				break

		print(nums[0])

def part_two():


		for noun in range(100):
			for verb in range(100):
				with open('day2.input') as file: #hecken slow and lazy way to maintain same nums
					nums = eval(file.read())
					nums = list(nums)
					

					nums[1] = noun
					nums[2] = verb
					for i in range(0,len(nums),4):
						# print(nums[i])

						opcode = nums[i]

						if opcode == 1: #addiition
							nums[nums[i+3]] = nums[nums[i+2]] + nums[nums[i+1]]

						if opcode == 2: 
							nums[nums[i+3]] = nums[nums[i+2]] * nums[nums[i+1]]

						if opcode == 99:
							break

					if nums[0] == 19690720:
						print(noun,verb)
						break

if __name__ == '__main__':
	part_two()