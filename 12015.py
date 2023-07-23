# 12015.py
# 23.07.23. 09:36 ~ x

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [0]

for x in lst:
	if x > dp[-1]:
		dp.append(x)
		continue
	left = 0
	right = len(dp)
	while left < right:
		mid = (left + right) // 2
		if dp[mid] < x:
			left = mid+1
		else:
			right = mid
	dp[right] = x
print(len(dp)-1)
