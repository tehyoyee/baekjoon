# 18111.py
# 23.01.17 02:35 ~ 03:46
# 71분

import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = []
height_high = 0
height_low = 256
for _ in range(n):
	a = list(map(int, input().split()))
	graph.append(a)
	height_high = max(height_high, max(a))
	height_low = min(height_low, min(a))
result = [float('inf'), 0]
for height in range(height_low, height_high + 1):
	dec_volume = 0
	inc_volume = 0
	for i in range(n):
		for j in range(m):
			if graph[i][j] > height:
				dec_volume += (graph[i][j] - height)
			else:
				inc_volume += (height - graph[i][j])
	if dec_volume + b < inc_volume:
		continue
	time = dec_volume * 2 + inc_volume
	if time <= result[0]:
		result = [time, height]
for x in result:
	print(x, end=" ")
