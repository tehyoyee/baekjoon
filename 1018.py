# 1018 py

def test(x, y, arr, color):
	result = 0
	for i in range(8):
		for j in range(8):
			if arr[x + i][y + j] == color and (i + j) % 2 == 0:
				result += 1
			elif arr[x + i][y + j] != color and (i + j) % 2 == 1:
				result += 1
	return result

a, b = map(int, input().split())
arr = []
result = []

for _ in range(a):
	arr.append(input())

for i in range(a - 7):
	for j in range(b - 7):
		result.append(test(i, j, arr, 'B'))
		result.append(test(i, j, arr, 'W'))

print(min(result))