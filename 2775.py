# 2775 py

t = int(input())
for _ in range(t):
	k = int(input())
	n = int(input())
	arr = []
	for i in range(n):
		arr.append(i + 1)
	for k in range(k):
		for i in range(1, n):
			arr[i] = arr[i] + arr[i - 1]
	print(arr[n - 1])
