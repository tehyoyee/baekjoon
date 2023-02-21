# 2470.py
# 23.02.21. 11:19 ~

n = int(input())
sols = list(map(int, input().split()))
sols.sort()
start = 0
end = n - 1
new_sol = 2000000000
while start < end:
	if (abs(sols[start] + sols[end]) < new_sol):
		new_sol = abs(sols[start] + sols[end])
		result = [sols[start], sols[end]]
	if abs(sols[start]) > abs(sols[end]):
		start += 1
	else:
		end -= 1
print(*result)