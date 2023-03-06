# 2668.py
# 23.03.06. 10:33 ~ 11:18

def dfs(s, i):
	if i == s:
		result.append(i)
		return True
	else:
		for ni in graph[i]:
			if not visit[ni] and dfs(s, ni):
				visit[ni] = True
				result.append(i)
				return True


n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[int(input())].append(i)
result = []
visit = [False] * (n + 1)
for i in range(1, n + 1):
	for x in graph[i]:
		if not visit[i]:
			visit[x] = True
			dfs(i, x)
print(len(result))
for x in sorted(result):
	print(x)