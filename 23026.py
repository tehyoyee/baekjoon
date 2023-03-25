# 23026.py
# 23.03.16. 16:24 ~

# import sys
# input = sys.stdin.readline

# def f(i, B, goods):
# 	if i + goods <= B:
# 		return i + goods
# 	else:
# 		return 0

# T = int(input())
# for _ in range(T):
# 	n, B, R = map(int, input().split())
# 	v = list(map(int, input().split()))
# 	cnt = 1
# 	i = 0
# 	for _ in range(R):
# 		for goods in v:
# 			i = f(i, B, goods)
# 			if not i:
# 				i = 0
# 				cnt += 1
# 				i = f(i, B, goods)
# 	print(cnt)




# import sys
# input = sys.stdin.readline

# def f(i, B, goods):
# 	if i + goods <= B:
# 		return i + goods
# 	else:
# 		return 0

# T = int(input())
# for _ in range(T):
# 	n, B, R = map(int, input().split())
# 	v = list(map(int, input().split()))
# 	box_cnt = 1
# 	i = 0
# 	truck_cnt = 1
# 	while True:
# 		for goods in v:
# 			i = f(i, B, goods)
# 			if not i:
# 				i = 0
# 				box_cnt += 1
# 				i = f(i, B, goods)
# 		if not f(i, B, v[0]):
# 			break
# 		truck_cnt += 1
# 	box = (R // truck_cnt) * box_cnt
# 	R %= truck_cnt
# 	if R:
# 		box += 1
# 		i = 0
# 		for _ in range(R):
# 			for goods in v:
# 				i = f(i, B, goods)
# 				if not i:
# 					i = 0
# 					box += 1
# 					i = f(i, B, goods)
# 	print(box)


# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
# 	n, B, R = map(int, input().split())
# 	v = list(map(int, input().split()))
# 	box_cnt = 1
# 	i = 0
# 	truck_cnt = 1
# 	rest = 1
# 	dp = [0]
# 	while True:
# 		for goods in v:
# 			i += goods
# 			if i > B:
# 				i = goods
# 				box_cnt += 1
# 		dp.append(box_cnt)
# 		if i + v[0] > B:
# 			break
# 		truck_cnt += 1
# 	box_cnt = (R // truck_cnt) * box_cnt
# 	box_cnt += dp[R % truck_cnt]
# 	print(box_cnt)


# import sys
# sys.setrecursionlimit(10**4)
# input = sys.stdin.readline

# def f(i, box_cnt, truck_cnt, R):
# 	if R < truck_cnt:
# 		return -1, -1, -1
# 	for goods in v:
# 		i += goods
# 		if i > B:
# 			i = goods
# 			box_cnt += 1
# 	dp.append(box_cnt)
# 	if i + v[0] > B:
# 		return i, box_cnt, truck_cnt
# 	truck_cnt += 1
# 	return f(i, box_cnt, truck_cnt, R)

# result = []
# T = int(input())
# for _ in range(T):
# 	n, B, R = map(int, input().split())
# 	v = list(map(int, input().split()))
# 	dp = [0]
# 	i, box_cnt, truck_cnt = f(0, 1, 1, R)
# 	if i == -1:
# 		print(dp[R])
# 		break
# 	box_cnt = (R // truck_cnt) * box_cnt
# 	box_cnt += dp[R % truck_cnt]
# 	result.append(box_cnt)
# for r in result:
# 	print(r)


# import sys
# sys.setrecursionlimit(10**4)
# input = sys.stdin.readline

# def f(i, box_cnt, truck_cnt, R):
# 	if R < truck_cnt:
# 		return -1, -1, -1
# 	for goods in v:
# 		i += goods
# 		if i > B:
# 			i = goods
# 			box_cnt += 1
# 	dp.append(box_cnt)
# 	if i + v[0] > B:
# 		return i, box_cnt, truck_cnt
# 	truck_cnt += 1
# 	return f(i, box_cnt, truck_cnt, R)

# result = []
# T = int(input())
# for _ in range(T):
# 	n, B, R = map(int, input().split())
# 	v = list(map(int, input().split()))
# 	dp = [0]
# 	i, box_cnt, truck_cnt = f(0, 1, 1, R)
# 	if i == -1:
# 		print(dp[R])
# 		break
# 	box_cnt = (R // truck_cnt) * box_cnt
# 	box_cnt += dp[R % truck_cnt]
# 	result.append(box_cnt)
# for r in result:
# 	print(r)


# import sys
# from collections import deque
# input = sys.stdin.readline

# result = []
# T = int(input())
# for _ in range(T):
# 	n, B, R = map(int, input().split())
# 	v = list(map(int, input().split()))
# 	dp = [0]
# 	tt = v[0]
# 	q = deque(v)
# 	box = 0
# 	box_cnt = 1
# 	truck_cnt = 1
# 	while truck_cnt <= R:
# 		cur = q.popleft()
# 		box += cur
# 		if box > B:
# 			box = cur
# 			box_cnt += 1
# 		if not q:
# 			if box + v[0] > B:
# 				break
# 			truck_cnt += 1
# 			dp.append(box_cnt)
# 			q = deque(v)
# 	box_cnt = (R // truck_cnt) * box_cnt + dp[R % truck_cnt]
# 	print(box_cnt)



# 	result.append(box_cnt)
# for r in result:
# 	print(r)


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	n, B, R = map(int, input().split())
	v = list(map(int, input().split()))
	box_cnt = 1
	i = 0
	truck_cnt = 1
	while True:
		for goods in v:
			i += goods
			if i > B:
				i = goods
				box_cnt += 1
		if i + v[0] > B:
			break
		truck_cnt += 1
	box_cnt = (R // truck_cnt) * box_cnt
	R %= truck_cnt
	if R:
		box_cnt += 1
		i = 0
		for _ in range(R):
			for goods in v:
				i += goods
				if i > B:
					i = goods
					box_cnt += 1
	print(box_cnt)