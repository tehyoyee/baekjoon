import sys
input = sys.stdin.readline

a = input()
b = input()
arr = [[0] * (len(b)) for _ in range(len(a))]
print(arr)
for i in range(1, len(a)):
	for j in range(1, len(b)):
		if a[i - 1] == b[j - 1]:
			arr[i][j] += arr[i - 1][j - 1] + 1
		else:
			arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

print(arr[-1][-1])

# 2차원 행렬을 통해 같았던 횟수를 더해나감.