# 7568py

t = int(input())
arr = []
for _ in range(t):
	arr.append(list(map(int, input().split())))

rank = [1] * t
for i in range(t):
	for j in range(t):
		if (arr[i][0] < arr[j][0]) and (arr[i][1] < arr[j][1]):
			rank[i] += 1
for i in rank:
	print(i, end=" ")