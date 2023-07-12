# 21921.py
# 23.07.12. 22:18 ~ 22:29

import sys
from collections import deque
input = sys.stdin.readline

N, X = map(int, input().split())
lst = list(map(int, input().split()))

q = deque()
resultCnt = 1
resultV = sum(lst[:X])
for i in range(X):
	q.append(lst[i])

sum_ = resultV
for x in lst[X:]:
	sum_ += x
	sum_ -= q.popleft()
	q.append(x)
	if sum_ == resultV:
		resultCnt += 1
	elif sum_ > resultV:
		resultV = sum_
		resultCnt = 1

if resultV:
	print(resultV)
	print(resultCnt)
else:
	print("SAD")