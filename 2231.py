# 2231 py

n = int(input())

length = len(str(n))
arr = []
if n - length * 9 > 0:
	for i in range(n - length * 9, n):
		result = i
		i = str(i)
		for x in i:
			result += int(x)
		if result == n:
			arr.append(int(i))
else:
	for i in range(0, n):
		result = i
		i = str(i)
		for x in i:
			result += int(x)
		if result == n:
			arr.append(int(i))
arr.sort()
if len(arr) == 0:
	print("0")
else:
	print(arr[0])