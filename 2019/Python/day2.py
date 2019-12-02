
def part_one():
	with open('day2.input') as file:
		nums = eval(file.read())
		nums = list(nums)

		nums[1] = 12
		nums[2] = 2
		for i in range(0,len(nums),4):
			# print(nums[i])

			opcode = nums[i]

			if opcode == ADD:
				nums[nums[i+3]] = nums[nums[i+2]] + nums[nums[i+1]]

			if opcode == MUL: 
				nums[nums[i+3]] = nums[nums[i+2]] * nums[nums[i+1]]

			if opcode == END:
				break

		print(nums[0])

def part_two():

		with open('day2.input') as file: #hecken slow and lazy way to maintain same nums
			orginal_nums = eval(file.read())
			orginal_nums = list(orginal_nums)
		def get_numbers():
			return orginal_nums.copy()

		for noun in range(100):
			for verb in range(100):
				nums = get_numbers()
					

				nums[1] = noun
				nums[2] = verb
				for i in range(0,len(nums),4):
					# print(nums[i])

					opcode = nums[i]

					if opcode == ADD: #addiition
						nums[nums[i+3]] = nums[nums[i+2]] + nums[nums[i+1]]

					if opcode == MUL: 
						nums[nums[i+3]] = nums[nums[i+2]] * nums[nums[i+1]]

					if opcode == END:
						break

				if nums[0] == 19690720:
					print(noun,verb)
					return

if __name__ == '__main__':

	ADD = 1
	MUL = 2
	END = 99
	part_one()
	part_two()