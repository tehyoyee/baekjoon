# 2252.py
# 23.02.15. 13:37 ~ 57, 14:22 ~ 14:45
# 위상정렬

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
visit = [False] * (n + 1)
q = []
result = []

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1
for i in range(1, n + 1):
	if indegree[i] == 0:
		q.append(i)
while q:
	cur = q.pop(0)
	result.append(cur)
	for i in graph[cur]:
		indegree[i] -= 1
		if indegree[i] == 0:
			q.append(i)
print(*result)