# 14891.py
# 23.02.20. 14:28 ~ 15:28

from collections import deque

gears = []
for _ in range(4):
    gears.append(deque(input()))

t = int(input())
for _ in range(t):
	status = [0] * 4
	n, d = map(int, input().split())
	n -= 1
	status[n] = d
	for i in range(3):
		if not (n + i + 1 < 4):
			break
		if gears[n + i][2] != gears[n + i + 1][6]:
			status[n + i + 1] = status[n + i] * -1
		else:
			break
	for i in range(3):
		if not (0 <= n - i - 1):
			break
		if gears[n - i][6] != gears[n - i - 1][2]:
			status[n - i - 1] = status[n - i] * -1
		else:
			break
	for i in range(4):
		if status[i] != 0:
			gears[i].rotate(status[i])
result = 0
for i in range(3, -1, -1):
	if gears[i][0] == '1':
		result += pow(2, i)
print(result)
