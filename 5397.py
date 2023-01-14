# 5397.py
# 23.01.15 00:52~
from collections import deque

t = int(input())
for _ in range(t):
	s = deque(input())
	result = deque()
	i = 0
	while s:
		tmp = s.popleft()
		if tmp == "<":
			if i > 0:
				i -= 1
		elif tmp == ">":
			if i < len(result):
				i += 1
		elif tmp == "-":
			if len(result) == 0 or i == 0:
				continue
			del result[i - 1]
			i -= 1
		elif i == len(result):
			result.append(tmp)
			i += 1
		else:
			result.insert(i, tmp)
			i += 1
	for x in result:
		print(x, end="")
	print()
	