
from collections import Counter

def solve(part):
	yes_pass = []
	for num in range(307237, 769058):
		str_num = str(num)
		if list(str_num) == sorted(str_num):
			for val in Counter(str_num).values():
				if (val >= 2 and part==1) or (val == 2 and part==2):
					yes_pass.append(str_num)
					break

	print(len(yes_pass))
if __name__ == '__main__':
	solve(1)
	solve(2)

	#Time to code golf
	r = range(307237, 769058)
	s = lambda a: list(str(a)) == sorted(str(a))
	o = lambda a: s(a) and any(x >= 2 for x in Counter(str(a)).values())
	t = lambda a: s(a) and any(x == 2 for x in Counter(str(a)).values())
	print(sum(map(t, r)),sum(map(o, r)))