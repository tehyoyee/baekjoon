# 2170.py
# 23.03.09. 16:09 ~ 16:40
# 입력 겹치는 거 지우기 위해 set으로 어펜드. sort 람다설정. 시간줄이기.

n = int(input())
pos = []
for _ in range(n):
	a, b = map(int, input().split())
	if a > b:
		a, b = b, a
	pos.append((a, b))
pos.sort(key=lambda x:x[0])
result = pos[0][1] - pos[0][0]
prevMax = pos[0][1]
for i in range(1, n):
	if prevMax < pos[i][1]:
		if prevMax < pos[i][0]:
			result += (pos[i][1] - pos[i][0])
		else:
			result += pos[i][1] - prevMax
		prevMax = pos[i][1]
print(result)
