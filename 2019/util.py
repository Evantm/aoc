from collections import defaultdict

def swap_dict(dictionary:dict) -> dict:
	temp = defaultdict(list)

	for key, value in dictionary.items():
		temp[value].append(key)

	return dict(temp)


def manhattan_dist 