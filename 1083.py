# 1083.py
# 23.06.29. 10:55 ~ 11:55 ㄷㅏㅂ지

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
S = int(input())

i = 0
while i != len(lst):
	if S <= 0:
		break
	target = i
	for j in range(i + 1, i + 1 + S):
		if j == len(lst):
			break
		if lst[target] < lst[j]:
			target = j
	S -= (target-i)
	x = lst[target]
	lst.remove(x)
	lst.insert(i, x)
	i += 1

print(*lst)
