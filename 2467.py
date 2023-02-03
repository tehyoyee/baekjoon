# 2467.py
# 23.02.03. 11:18 ~ 11:33

n = int(input())
sol = list(map(int, input().split()))

i = 0
j = n - 1
a, b = sol[0], sol[n - 1]
diff = abs(a + b)

	
while True:
	if sol[i] + sol[j] > 0:
		j -= 1
	else:
		i += 1
	if i == j:
		break
	if diff > abs(sol[i] + sol[j]):
		a = sol[i]
		b = sol[j]
		diff = abs(a + b)
print(a, b)