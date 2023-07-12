# 2357.py
# 23.07.06. ~ re

import sys
import math
input = sys.stdin.readline

def initSeg(i, s, e):
	if s == e:
		seg[i] = (lst[s], lst[s])
		return seg[i]
	
	mid = (s + e) // 2

	l = initSeg(i * 2, s, mid)
	r = initSeg(i * 2 + 1, mid + 1, e)

	seg[i] = (min(l[0], r[0]), max(l[1], r[1]))
	return seg[i]

def f(s, e, i):
	if e < a or b < s:
		return (1000000000, 0)
	
	mid = (s + e) // 2

	if a <= s and e <= b:
		return seg[i]
	
	else:
		l = f(s, mid, i * 2)
		r = f(mid + 1, e, i * 2 + 1)
		return (min(l[0], r[0]), max(l[1], r[1]))

N, M = map(int, input().split())
lst = []
for _ in range(N):
	lst.append(int(input()))

H = math.ceil(math.log2(N)) + 1
nodeCnt = 1 << H
seg = [0] * nodeCnt
initSeg(1, 0, len(lst) - 1)

print(seg)
print()

for _ in range(M):
	a, b = map(int, input().split())
	a, b = a - 1, b - 1
	result = f(0, len(lst) - 1, 1)
	print(result[0], result[1])