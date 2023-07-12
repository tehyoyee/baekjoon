# 10986.py
# 23.07.12. 21:00 ~ x

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

sum_list = [0 for _ in range(1000)]
sum_list[0] = 1

sum_ = 0
result = 0

for x in lst:
	sum_ += x
	result += sum_list[sum_ % K]
	sum_list[sum_ % K] += 1

print(result)