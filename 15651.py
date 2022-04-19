# 15651 py

def comb(n, m, s):
	if len(arr) == m:
		print(" ".join(map(str, arr)))
		return
	for i in range(1, n + 1):
		arr.append(i)
		comb(n, m, i)
		arr.pop()

n, m = map(int, input().split())
arr = []
comb(n, m, 1)