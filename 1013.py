# 1013.py
# 23.03.12. 16:38 ~ 17:13

# (100+1+ | 01)+


import sys
input = sys.stdin.readline

def dfs(i, end):
	result = 0
	if pattern[i:i + 2] == "01":
		dfs(i + 2, end)
	if i + 4 < end and pattern[i:i + 2] == "10":
		j = 2
		if not pattern[i + j] == '0':
			break
		while if i + j <= i_pattern[i + j] == '0':
			j += 1
		while pattern[i + j] == '1':
			j += 1
		
	return 0

N = int(input())
for _ in range(N):
	pattern = input()
	print(dfs())