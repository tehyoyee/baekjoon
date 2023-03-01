# 14719.py
# 23.03.01. 18:59 ~ 17:37

import sys
from collections import deque
input = sys.stdin.readline

def right(idx, w, depth):
	j = 0
	while True:
		if not 0 <= idx + j < w:
			return 0
		if graph[idx + j] >= depth:
			return 1
		j += 1

def left(idx, w, depth):
	j = 0
	while True:
		if not 0 <= idx - j < w:
			return 0
		if graph[idx - j] >= depth:
			return 1
		j += 1
            
def findDepth(idx, h, w):
	for d in range(h, 0, -1):
		if graph[idx] == d:
			return 0
		tmp = right(idx, w, d) + left(idx, w, d)
		if tmp == 2:
			return d - graph[idx]
	return 0

h, w = map(int, input().split())
graph = list(map(int, input().split()))
visit = [0] * w
depths = []

for k in range(w):
	depths.append(findDepth(k, h, w))
print(sum(depths))