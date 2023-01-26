# 9019.py
# 23.01.26. 20:59 ~
# import sys
# input = sys.stdin.readline

# t = int(input())

# def cal_D(d):
# 	return (d * 2) % 10000

# def cal_S(d):
# 	if d == 0:
# 		return 9999
# 	else:
# 		return d - 1

# def cal_L(d):
# 	return (d * 10) % 10000 + d // 1000

# def cal_R(d):
# 	return (d // 10) + (d % 10) * 1000

# f = [cal_D, cal_S, cal_L, cal_R]
# n = ['D', 'S', 'L', 'R']

# def s(a, b, path):
# 	q = [[a, path]]
# 	visit[a] = True
# 	while q:
# 		a_c, path_c = q.pop(0)
# 		if a_c == b:
# 			return path_c
# 		for k in range(4):
# 			tmp = f[k](a_c)
# 			if not visit[tmp]:
# 				q.append([tmp, path_c + n[k]])
# 				visit[a_c] = True
# 	return 0

# for _ in range(t):
# 	visit = [0] * 10000
# 	a, b = map(int, input().split())
# 	print(s(a, b, ""))

# from collections import deque
# import sys
# input = sys.stdin.readline

# t = int(input())
# n = ['D', 'S', 'L', 'R']

# def cal(d, i):
# 	if i == 0:
# 		return (d * 2) % 10000
# 	elif i == 1:
# 		if d == 0:
# 			return 9999
# 		else:
# 			return d - 1
# 	elif i == 2:
# 		return (d * 10) % 10000 + d // 1000
# 	else:
# 		return (d // 10) + (d % 10) * 1000

# def s(a, b, path):
# 	q = deque()
# 	q.append([a, path])
# 	visit[a] = True
# 	while q:
# 		a_c, path_c = q.popleft()
# 		if a_c == b:
# 			print(path_c)
# 			return
# 		for k in range(4):
# 			tmp = cal(a_c, k)
# 			if not visit[tmp]:
# 				q.append([tmp, path_c + n[k]])
# 				visit[a_c] = True

# for _ in range(t):
# 	visit = [False] * 10000
# 	a, b = map(int, input().split())
# 	s(a, b, "")


from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
n = ['D', 'S', 'L', 'R']

def cal(d, i):
	if i == 'D':
		return (d * 2) % 10000
	elif i == 'S':
		if d == 0:
			return 9999
		else:
			return d - 1
	elif i == 'L':
		return (d * 10) % 10000 + d // 1000
	elif i == 'R':
		return (d // 10) + (d % 10) * 1000

def s(a, b, path):
	q = deque()
	q.append([a, path])
	visit[a] = True
	while q:
		a_c, path_c = q.popleft()
		if a_c == b:
			print(path_c)
			return
		for cmd in n:
			tmp = cal(a_c, cmd)
			if not visit[tmp]:
				q.append([tmp, path_c + cmd])
				visit[tmp] = True

for _ in range(t):
	visit = [False] * 10000
	a, b = map(int, input().split())
	s(a, b, "")