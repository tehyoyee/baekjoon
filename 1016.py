# 1016.py
# 23.08.22. 14:14 ~

MIN, MAX = map(int, input().split())
result = MAX - MIN + 1
table = [False] * (MAX - MIN + 1)
for i in range(2, int((MAX)**0.5)+1):
	x = i ** 2
	j = MIN // x - 1
	if MIN % x == 0:
		j += 1
	k = x * j
	print(i, k)
	while k <= MAX:
		if not table[x-MIN]:
			table[x-MIN] = True
			result -= 1
		k += x
	i += 1
print(result)
