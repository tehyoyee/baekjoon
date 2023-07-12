# 1991.py
# 23.07.09. 20:08 ~

import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
graph = [[] for i in range(N)]

for _ in range(N):
	a, b, c = input().split()
	graph[ord(a)-ord('A')].append(ord(b) - ord('A'))
	graph[ord(a)-ord('A')].append(ord(c) - ord('A'))

def dfs(ci, mode):
	if mode == 0:
		print(chr(ci + ord('A')), end='')
	ni = graph[ci][0]
	if ni > 0 and not visit[ni]:
		visit[ni] = True
		dfs(ni, mode)
	if mode == 1:
		print(chr(ci + ord('A')), end='')
	ni = graph[ci][1]
	if ni > 0 and not visit[ni]:
		visit[ni] = True
		dfs(ni, mode)
	if mode == 2:
		print(chr(ci + ord('A')), end='')
	
for i in range(3):
	visit = [False] * N
	visit[0] = True
	dfs(0, i)
	print()