# 20055.py
# 23.03.02. 17:08 ~ 17:43

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False] * n)
cnt = 0
distoried = 0
for b in belt:
	if b == 0:
		distoried += 1
while distoried < k:
	cnt += 1
	belt.rotate(1)
	robot.rotate(1)
	robot[n - 1] = False
	for i in range(n - 2, 0, -1):
		if robot[i] and not robot[i + 1] and belt[i + 1]:
			robot[i], robot[i + 1] = False, True
			robot[n - 1] = False
			belt[i + 1] -= 1
			if belt[i + 1] == 0:
				distoried += 1
	if belt[0]:
		robot[0] = True
		belt[0] -= 1
		if belt[0] == 0:
			distoried += 1
print(cnt)