# 1181.py
# 23.07.06. 20:48 ~ 20:52

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
	s = input().rstrip()
	lst.append((len(s), s))
lst = list(set(lst))
lst.sort(key = lambda x:(x[0],x[1]))
for x in lst:
	print(x[1])	