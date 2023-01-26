# 2343.py
# 23.01.22. 20:24 ~

n, m = map(int, input().split())
lst = list(map(int, input().split()))
start = 0
end = sum(lst)

def check(mid, n, m):
	for i in range(n):
		tmp += lst[i]
		if tmp >= mid:
			chunk += 1
			tmp = 0
		elif i == n - 1 and tmp > 0:
			chunk += 1
			ca.append(tmp + lst[i])
	if mid == m:
		return True
	else:
		return False

while True:
	mid = (start + end) // 2
	chunk = 0
	tmp = 0
	print(start, end, mid)
	else:
		break
print(max(ca))