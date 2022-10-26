# 15954.py

# def sqrt(n):
# 	result = 0
# 	n = n * 10 ** 12
# 	ref = str(n)[0:2]
# 	ref = float(ref)
# 	print(ref)
# 	n *= 10**12
# 	# print(n)

n, k = map(int, input().split())
a = list(map(int ,input().split()))
result = []
for i in range(0, n - 2):
	temp = 0
	m = sum(a[i:i+k]) / k
	for j in range(3):
		temp += (a[i + j] - m) ** 2
	result.append(pow(temp / k, 1/2))
print(str(min(result))[0:10])
# print(pow(4,1/2))