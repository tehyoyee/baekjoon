# 2805.py

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.append(0)
tree.sort(reverse = True)
dp = [0]
for i in range(0, n):
	dp.append(dp[i] + (tree[i] - tree[i + 1]) * (i + 1))
start = 1
end = n
while True:
	pivot = (start + end) // 2
	if dp[pivot - 1] < m <= dp[pivot]:
		break
	if m < dp[pivot]:
		end = pivot - 1
	else:
		start = pivot + 1
print(tree[pivot] + (dp[pivot] - m) // pivot)

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# tree = list(map(int, input().split()))
# tree.append(0)
# tree.sort(reverse = True)
# dp = []
# for i in range(n + 1):
# 	dp.append(sum(tree[:i]) - tree[i]*(i))
# print(dp)
# start = 1
# end = n
# while True:
# 	pivot = (start + end) // 2
# 	if dp[pivot - 1] < m <= dp[pivot]:
# 		break
# 	if m < dp[pivot]:
# 		end = pivot - 1
# 	else:
# 		start = pivot + 1
# print(tree[pivot] + (dp[pivot] - m) // pivot)