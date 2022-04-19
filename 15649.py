# 15649py

def comb(n, m):
	if m == 0:
		print(" ".join(map(str, arr)))
		return
	for x in range(1, n + 1):
		if not x in arr:
			arr.append(x)
			comb(n, m - 1)
			arr.pop()

n, m = map(int, input().split())
arr = []

comb(n, m)