# 1068.py
# 23.02.02 09:36 ~ 11:06

def bfs(i, target):
	result = 0
	q = [[i, 0]]
	while q:
		cur, layer = q.pop(0)
		if len(tree[cur]) == 0 and layer != 0:
			result += 1
		for x in tree[cur]:
			if x != target:
				q.append([x, layer + 1])
			elif len(tree[cur]) == 1:
				result += 1
	return result

n = int(input())
graph = list(map(int, input().split()))
tree = [[] for _ in range(n)]
root = []
target = int(input())
i = 0
for x in graph:
	if x == -1:
		root.append(i)
	else:
		tree[x].append(i)
	i += 1
tree[target] = []
result_t = 0
for x in root:
	result_t += bfs(x, target)
print(result_t)
