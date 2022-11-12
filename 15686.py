# 15686.py

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from itertools import combinations

n, m = map(int, input().split())
graph = []
chickens = []
houses = []

def bfs(i, j, steps):
	q = [[i, j]]
	while q:
		i_cur, j_cur = q.pop(0)
		

for i in range(n):
	graph.append(list(map(int, input().split())))
	for j in range(n):
		if graph[i][j] == 2:
			chickens.append([i, j])
		elif graph[i][j] == 1:
			houses.append([i, j])
print(chickens)
coms = combinations(chickens, m)
result = 0
for com in coms:
	dis_com = 1000000
	for house in houses:
		dis = 1000000
		for chicken in chickens:
			dis = min(dis, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
		dis_com += dis
	result += dis_com
print(list(arr))