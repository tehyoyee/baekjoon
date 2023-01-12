# 1654.py

def count(pivot):
	result = 0
	for x in arr:
		result += x // pivot
	return result

k, n = map(int, input().split())
arr = []
for _ in range(k):
	arr.append(int(input()))
arr.sort()

pivot = sum(arr) // n
print()
print(pivot)
print(count(pivot))
print(arr)