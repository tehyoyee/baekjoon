# 1715.py

# import sys
# input = sys.stdin.readline
# from collections import deque

# n = int(input())
# arr = []
# for _ in range(n):
# 	arr.append(int(input()))
# arr.sort()
# q = deque(arr)
# result = 0

# while n >= 2:
# 	i = 0
# 	a = q.popleft()
# 	b = q.popleft()
# 	result += (a + b)
# 	a += b
# 	for _ in range(n - 2):
# 		if a < q[0]:
# 			break
# 		i += 1
# 		q.rotate(-1)
# 	q.appendleft(a)
# 	q.rotate(i)
# 	n -= 1
# 	print(q)

# print(result)

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
heap = []
for _ in range(n):
	heappush(heap, int(input()))

result = 0
while n >= 2:
	a = heappop(heap)
	a += heappop(heap)
	result += a
	heappush(heap, a)
	n -= 1

print(result)
