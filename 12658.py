# 12658.py

import sys
input = sys.stdin.readline
t = int(input())
basins = []
for i in range(26):
	basins.append(chr(ord('a') + i))
for _ in range(t):
	m, n = map(int, input().split())
	graph = []
	for _ in range(m):
		graph.append(list(map(int, input().split())))
