# 12865.py

import sys
import copy
input = sys.stdin.readline

def search(goods, ref, dp):
	for i in range(len(goods)):
		if ref + goods[i][0] <= k:
			temp = copy.deepcopy(goods)
			temp.pop(i)
			dp[ref + goods[i][0]] = max(dp[ref] + goods[i][1], dp[ref + goods[i][0]])
			search(temp, ref + goods[i][0], dp)

n, k = map(int, input().split())
goods = []
dp = [0] * (k + 1)
for _ in range(n):
	a, b = map(int, input().split())
	goods.append([a, b])

search(copy.deepcopy(goods), 0, dp)
print(max(dp))