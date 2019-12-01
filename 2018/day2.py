
def part_one():
	from collections import Counter
	two_count = 0
	three_count = 0

	with open("day2.input") as file:
		for word in file:
			c = Counter(word[:-1])
			for key,val in c.items():
				if val == 2:
					two_count += 1
					break

			for key,val in c.items():
				if val == 3:
					three_count += 1
					break
	print(three_count*two_count)

def part_two():

	def list_difference(word1,word2):
		return [i for i in word1 if i not in word2]

	def list_same(word1,word2):
		same = ''
		for i,j in zip(word1,word2):
			if i == j:
				same += i
		return same

	words = []
	common_words = []
	with open("day2.input") as file:
		for word in file:
			words.append(word[:-1])
	for word1 in words:
		for word2 in words:
			if word1 != word2:
				if (len(word1) - len(list_same(word1,word2)) == 1):
					common_words.append(word1)

	print(list_same(*common_words))

if __name__ == '__main__':
	part_two()