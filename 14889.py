# 14889py

from itertools import combinations

min = 1000
graph = []

def dfs(n):
	candidate = [i for i in range(n)]

	for comb in combinations(candidate, n // 2):
		start = set(comb)
		link = set(candidate) - start
		start = list(start)
		link = list(link)

		result(start, link, 0, 0)
	
def result(start, link, start_sum, link_sum):
	global graph
	global min

	for i in start:
		for j in start:
			start_sum += graph[i][j]
	for i in link:
		for j in link:
			link_sum += graph[i][j]
	if abs(start_sum - link_sum) < min:
		min = abs(start_sum - link_sum)

n = int(input())

for _ in range(n):
	graph.append(list(map(int, input().split())))

dfs(n)
print(min)