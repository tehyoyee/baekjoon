# 2166.py
# 23.02.08. 12:54 ~ 답지 봄봄

n = int(input())
result = 0.0
lines = []
for _ in range(n):
	lines.append(list(map(int, input().split())))
lines.append([lines[0][0], lines[0][1]])
for i in range(n):
	result = result + lines[i][0] * lines[i + 1][1] - lines[i + 1][0] * lines[i][1]
result = abs(result) / 2

print(round(result, 1))