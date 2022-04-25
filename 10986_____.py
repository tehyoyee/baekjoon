# 10986 py

import sys
input = sys.stdin.readline

def make_sum_list(nums, nums_sum):
	temp = nums[0] 
	nums_sum.append(temp)
	for i in range(1, len(nums)):
		temp += nums[i]
		nums_sum.append(temp)

result = 0
nums_sum = [0]
n, m = map(int ,input().split())
nums = list(map(int, input().split()))
for i in range(n):
	nums[i] = nums[i] % m
make_sum_list(nums, nums_sum)
for i in range(n + 1):
	for j in range(i + 1, n + 1):
		if (nums_sum[j] - nums_sum[i]) % m == 0:
			result += 1

print(result)
