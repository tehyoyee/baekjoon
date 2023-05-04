# 1300.py
# 23.05.04. 09:46 ~ x

N = int(input())
k = int(input())

start = 1
end = N**2
while start <= end:
	mid = (end + start) // 2
	cnt = 0
	for i in range(1, N+1):
		cnt += min(mid//i, N)
	if cnt >= k:
		end = mid-1
	else:
		start = mid+1
print(start)

# 1 2 2 3 3 4 6 6 9