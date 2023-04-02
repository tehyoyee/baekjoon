# 14499.py
# 23.04.02. 16:19 ~ 90분정도

import sys
input = sys.stdin.readline
from collections import deque

N, M, x, y, K = map(int, input().split())
graph = []
for _ in range(N):
	graph.append(list(map(int, input().split())))
path = deque(list(map(int, input().split())))
dice = [deque([0, 0, 0, 0]), 0, 0]
direction = 3

def diceTrans():
	tmp = []
	tmp.append(dice.pop())
	tmp.append(dice.pop())

	dice[0].rotate(1)
	dice.append(dice[0].popleft())
	dice[0].append(tmp.pop())
	dice[0].rotate(-1)
	dice.append(dice[0].popleft())
	dice[0].append(tmp.pop())
	dice[0].rotate(2)

while path:
	pathCur = path.popleft()
	if pathCur <= 2 and direction == 3:
		diceTrans()
		direction = 1
	elif pathCur >= 3 and direction == 1:
		diceTrans()
		direction = 3
	if pathCur == 1:
		y += 1
		if y > M - 1:
			y -= 1
			continue
		dice[0].rotate()
	elif pathCur == 2:
		y -= 1
		if y < 0:
			y += 1
			continue
		dice[0].rotate(-1)
	elif pathCur == 3:
		x -= 1
		if x < 0:
			x += 1
			continue
		dice[0].rotate(-1)
	elif pathCur == 4:
		x += 1
		if x > N - 1:
			x -= 1
			continue
		dice[0].rotate()
	if graph[x][y] == 0:
		graph[x][y] = dice[0][2]
	else:
		dice[0][2] = graph[x][y]
		graph[x][y] = 0
	print(dice[0][0])

# diceTrans()
# print(dice)
# diceTrans()
# print(dice)
# diceTrans()
# print(dice)
# diceTrans()
# print(dice)
