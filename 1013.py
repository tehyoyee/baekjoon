# 1013.py
# 23.03.12. 16:38 ~ 17:13
# 23.03.13. 09:58 ~ 49

# (100+1+ | 01)+

import sys
input = sys.stdin.readline

def dfs(i, end):
	result = 0
	if i == end:
		return i
	if pattern[i:i + 2] == "01":
		if i + 2 == end:
			return i + 2
		else:
			result = max(result, dfs(i + 2, end))
	elif i + 4 <= end and pattern[i:i + 2] == "10":
		i += 2
		if pattern[i] != '0':
			return 0
		while pattern[i] == '0':
			i += 1
			if i == end:
				return 0
		while pattern[i] == "1":
			result = max(dfs(i + 1, end), result)
			i += 1
			if i == end:
				return i
	return result

N = int(input())
for _ in range(N):
	pattern = input().rstrip()
	if dfs(0, len(pattern)) == len(pattern):
		print("YES")
	else:
		print("NO")