# 15650 py

def comb(n, m, s):
	if len(arr) == m:
		print(" ".join(map(str, arr)))
		return
	for i in range(s, n + 1):
		if i not in arr:
			arr.append(i)
			comb(n, m, i + 1)
			arr.pop()

n, m = map(int, input().split())
arr = []
comb(n, m, 1)