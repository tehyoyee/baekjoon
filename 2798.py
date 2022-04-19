# 2798 py

n, m = map(int, input().split())
arr = list(map(int, input().split()))
list_ = []
for i in range(n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
			if arr[i] + arr[j] + arr[k] <= m:
				list_.append(arr[i] + arr[j] + arr[k])
list_.sort()
print(list_[-1])