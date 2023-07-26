# 2188.py
# 23.07.25. 16:50 ~ 17:09

import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)

result = 0
N, M = map(int, input().split())
cows = [[] for _ in range(N + 1)]
visit = [0] * (M + 1)
visit2 = [False] * (N + 1)

def pushCow(i, cow):
	if not visit[i]:
		visit[i] = cow
		return True
	while cows[visit[i]]:
		if pushCow(cows[visit[i]].popleft(), visit[i]):
			visit[i] = cow
			return True
	return False

for i in range(1, N + 1):
	cows[i] = deque(list(map(int, input().split())))
	cows[i].popleft()

for i in range(1, N + 1):
	# while cows[i]:
	pushCow(cows[i].popleft(), i)
		# visit[i] = i
		# break

for i in range(1, M + 1):
	if visit[i]:
		result += 1
print(result)


# import sys

# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# def dfs(idx, visited, barn, caw):
#     if visited[idx] == True:
#         return 0
#     visited[idx] = True

#     for favor in caw[idx]:
#         if barn[favor] == 0 or dfs(barn[favor], visited, barn, caw):
#             barn[favor] = idx
#             return True
#     return False
    
# def solution():
# 	n, m = map(int, input().split())
# 	caw = [[] for _ in range(n+1)]
# 	barn = [0]*(m+1)

# 	for i in range(1, n+1):
# 		caw[i] = list(map(int, input().split()))[1:]
# 	for i in range(1, n+1):
# 		visited = [False]*(n+1)
# 		dfs(i, visited, barn, caw)
# 		print(barn)
# 	cnt = 0
# 	for i in barn:
# 		if i > 0:
# 			cnt += 1
# 	print(cnt)

# solution()


# 50 40
# 2 24 21
# 2 39 39
# 4 30 31 15 18
# 2 21 3
# 4 21 40 39 30
# 1 20
# 5 20 30 4 29 25
# 3 39 9 33
# 1 32
# 5 27 22 36 2 11
# 1 9
# 5 35 29 14 38 1
# 3 28 22 1
# 4 18 20 29 22
# 3 5 11 38
# 3 36 30 36
# 5 9 17 35 10 19
# 3 18 31 7
# 3 4 36 30
# 4 24 12 9 14
# 4 28 2 2 27
# 3 13 16 2
# 3 6 37 39
# 4 5 26 15 16
# 3 25 6 36
# 2 9 31
# 4 17 6 7 17
# 5 27 4 13 29 30
# 1 1
# 1 12
# 5 3 1 38 8 5
# 3 14 12 12
# 3 17 39 12
# 3 30 15 26
# 2 21 3
# 3 7 6 11
# 2 28 13
# 2 25 16
# 3 19 16 16
# 1 13
# 5 39 24 34 29 33
# 2 40 10
# 3 6 35 40
# 1 37
# 2 24 35
# 4 11 22 3 29
# 3 19 7 16
# 1 14
# 1 38
# 5 31 14 28 19 6