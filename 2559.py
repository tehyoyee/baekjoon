# 2559 py

n, m = map(int, input().split())
temp = list(map(int, input().split()))

sum_ = 0
temp_sum = [0]
temp_sum_range = []
for x in temp:
	sum_ += x
	temp_sum.append(sum_)
for i in range(m, len(temp_sum)):
	temp_sum_range.append(temp_sum[i] - temp_sum[i - m])
print(max(temp_sum_range))