# 17651.py
# 23.07.09. 16:56 ~

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
	lst.append(list(map(int, input().split())))
for x, y in sorted(lst, key=lambda x:(x[1], x[0])):
	print(x, y)