# 13023.py
# 23.01.26. 16:30 ~ 답지봄

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
flag = 0
def dfs(i, l, visit):
    visit[i] = 1
    if l == 4:
        return l
    for x in graph[i]:
        if not visit[x]:
            if dfs(x, l + 1, visit) == 4:
                return 4
            visit[x] = 0
    return l
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for x in range(n):
    # visit = [0] * n
	# print(dfs(x, 0, [0]*n))
    if dfs(x, 0, [0]*n) == 4:
        flag = 1
        break
print(flag)


# def bfs(i):
# 	l = 1
# 	q = [[i, l]]
# 	visit[i] = 1
# 	while q:
# 		i_c, l_c = q.pop(0)
# 		visit[i_c] = 1
# 		l = l_c
# 		for k in graph[i_c]:
# 			if not visit[k]:
# 				q.append([k, l_c + 1])
# 	return l

# # visit = [0] * n
# # print(bfs(4))

# for i in range(n):
# 	visit = [0] * n
# 	if bfs(i) >= 5:
# 		flag = 1
# 		break