# 6549.py
# 23.05.04. 11:26 ~

import sys
input = sys.stdin.readline

def check(i, idx):
	for j in range(i, i + idx):
		if graph[j] < idx:
			return False
	return True

while True:
	graph = list(map(int, input().split()))
	if graph[0] == 0:
		break
	w = graph[0]
	dp = [0] * (w + 1)
	for i in range(1, w + 1):
		 		