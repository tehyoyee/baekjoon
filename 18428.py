# 18428.py
# 23.04.28. 10:11 ~

# import sys
# input = sys.stdin.readline
# from collections import deque
# from itertools import combinations

# di = [0, 0, 1, -1]
# dj = [1, -1, 0, 0]

# N = int(input())
# graph = []
# teachers = []
# students = []
# for i in range(N):
# 	graph.append(list(input().split()))
# 	for j in range(N):
# 		if graph[i][j] == 'S':
# 			students.append([i, j])
# 		elif graph[i][j] == 'T':
# 			teachers.append([i, j])
# candi = []
# for ci, cj in teachers:
# 	for k in range(4):
# 		tmp = []
# 		for l in range(1, N):
# 			ni, nj = ci + l * di[k], cj + l * dj[k]
# 			if 0 <= ni < N and 0 <= nj < N:
# 				if graph[ni][nj] == 'S':
# 					candi += tmp
# 					break
# 				elif graph[ni][nj] == 'T':
# 					break
# 				tmp.append((ni, nj))
# 			else:
# 				break

# if len(candi) >= 3:
# 	candi = deque(list(combinations(candi, 3)))
# elif len(candi) == 2:
# 	candi = deque(list(combinations(candi, 2)))
# else:
# 	candi = deque([candi])
# while candi:
# 	three = list(candi.popleft())
# 	for ci, cj in three:
# 		graph[ci][cj] = 'O'
# 	isVisable = False
# 	for ci, cj in students:
# 		for k in range(4):
# 			for l in range(1, N):
# 				ni, nj = ci + l * di[k], cj + l * dj[k]
# 				if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] != 'S':
# 					if graph[ni][nj] == 'O':
# 						break
# 					if graph[ni][nj] == 'T':
# 						isVisable = True
# 						break
# 			if isVisable:
# 				break
# 		if isVisable:
# 			break
# 	if not isVisable:
# 		print("YES")
# 		exit()
# 	for ci, cj in three:
# 		graph[ci][cj] = 'X'
	
# print("NO")


import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

N = int(input())
candi = []
graph = []
teachers = []
students = []
for i in range(N):
	graph.append(list(input().split()))
	for j in range(N):
		if graph[i][j] == 'S':
			students.append([i, j])
		elif graph[i][j] == 'T':
			teachers.append([i, j])
		else:
			candi.append([i, j])

if len(candi) >= 3:
	candi = deque(list(combinations(candi, 3)))
elif len(candi) == 2:
	candi = deque(list(combinations(candi, 2)))
else:
	candi = deque([candi])
while candi:
	three = list(candi.popleft())
	for ci, cj in three:
		graph[ci][cj] = 'O'
	isVisable = False
	for ci, cj in students:
		for k in range(4):
			for l in range(1, N):
				ni, nj = ci + l * di[k], cj + l * dj[k]
				if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] != 'S':
					if graph[ni][nj] == 'O':
						break
					if graph[ni][nj] == 'T':
						isVisable = True
						break
			if isVisable:
				break
		if isVisable:
			break
	if not isVisable:
		print("YES")
		exit()
	for ci, cj in three:
		graph[ci][cj] = 'X'
	
print("NO")