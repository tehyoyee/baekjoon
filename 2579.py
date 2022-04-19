# 2579py

import sys

input = sys.stdin.readline

t = int(input())
point = []
cost = [[0] * 2 for i in range(t)]

for i in range(t):
	point.append(int(input()))

if t >= 1:
	cost[0][0] = point[0]
	cost[0][1] = point[0]
if t >= 2:
	cost[1][0] = point[1]
	cost[1][1] = point[0] + point[1]
	for i in range(2, t):
		cost[i][0] = point[i] + max(cost[i - 2][0], cost[i - 2][1])
		cost[i][1] = point[i] + cost[i - 1][0]

print(max(cost[t - 1]))
