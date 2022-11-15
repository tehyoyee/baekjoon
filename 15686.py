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
coms = combinations(chickens, m)
result = 1000000
coms = list(coms)
for i in range(len(coms)):
	dis = 0
	dis_sum = 0
	for house in houses:
		dis = 100000
		for j in range(len(coms[i])):
			dis = min(dis, abs(house[0] - coms[i][j][0]) + abs(house[1] - coms[i][j][1]))
		dis_sum += dis
	result = min(result, dis_sum)
print(result)