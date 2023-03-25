# 17609.py
# 23.03.13. 11:19 ~ 11:50

import sys
input = sys.stdin.readline

def s(i, j, cnt):
	result = 0
	if cnt == 2:
		return cnt
	while i < j and string[i] == string[j]:
		i += 1
		j -= 1
	if i >= j:
		return cnt
	else:
		result = (s(i, j - 1, cnt + 1))
		if result != 1:
			result = (s(i + 1, j, cnt + 1))
	return result

N = int(input())
for _ in range(N):
	string = input().rstrip()
	print(s(0, len(string) - 1, 0))