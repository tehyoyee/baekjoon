# 9466.py

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(s, i, l):
	result = 0
	if visit[i] == 1:
		if s == i:
			return l
		return 0
	visit[i] = 1
	if len(graph[i]):
		for x in graph[i]:
			result += dfs(s, x, l + 1)
	return result

t = int(input())
for _ in range(t):
	result = 0
	n = int(input())
	visit = [0] * (n + 1)
	lst = [0] + list(map(int, input().split()))
	graph = [[] for _ in range(n + 1)]
	for i in range(1, n + 1):
		graph[lst[i]].append(i)
	del(lst)

	for i in range(1, n + 1):
		if visit[i] == 0:
			result += dfs(i, i, 0)

	print(n - result)

## 메모리 초과

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**8)

# def dfs(i, path):
# 	visit[i] = 1
# 	for j in range(len(path)):
# 		if path[j] == lst[i]:
# 			return len(path[j:])
# 	if visit[lst[i]] == 0:
# 		return (dfs(lst[i], path+[lst[i]]))
# 	return 0

# t = int(input())
# for _ in range(t):
# 	result = 0
# 	n = int(input())
# 	visit = [0] * (n + 1)
# 	lst = [0] + list(map(int, input().split()))
# 	for i in range(1, n + 1):
# 		if visit[i] == 0:
# 			result += dfs(i, [i])
# 	print(n - result)


## 79퍼에서 메모리초과

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**5)

# def dfs(i):
# 	visit[i] = 1
# 	for j in range(len(path)):
# 		if path[j] == lst[i]:
# 			return len(path[j:])
# 	if visit[lst[i]] == 0:
# 		path.append(lst[i])
# 		return (dfs(lst[i]))
# 	return 0

# t = int(input())
# for _ in range(t):
# 	n = int(input())
# 	result = n
# 	visit = [0] * (n + 1)
# 	lst = [0] + list(map(int, input().split()))
# 	for i in range(1, n + 1):
# 		if visit[i] == 0:
# 			path = [i]
# 			result -= dfs(i)
# 	print(result)





# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# global result

# def dfs(s, i, l):
# 	global result
# 	if visit[i] == 1:
# 		if s == i:
# 			result += l
# 			return
# 		else:
# 			return 
# 	visit[i] = 1
# 	if len(graph[i]):
# 		for x in graph[i]:
# 			dfs(s, x, l + 1)

# t = int(input())
# for _ in range(t):
# 	result = 0
# 	n = int(input())
# 	visit = [0] * (n + 1)
# 	lst = [0] + list(map(int, input().split()))
# 	graph = [[] for _ in range(n + 1)]
# 	for i in range(1, n + 1):
# 		graph[lst[i]].append(i)
# 	del(lst)

# 	for i in range(1, n + 1):
# 		if visit[i] == 0:
# 			dfs(i, i, 0)

# 	print(n - result)
