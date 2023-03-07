# 3020.py
# 23.03.06. 13:51 ~ x 시간초과

N, H = map(int, input().split())
dp1 = [0] * H
dp2 = [0] * H
r1, r2 = N, 0
for i in range(N):
	if i % 2 == 0:
		dp1[int(input()) - 1] += 1
	else:
		dp2[H - int(input())] += 1
for i in range(H - 2, -1, -1):
	dp1[i] += dp1[i + 1]
for i in range(1, H):
	dp2[i] += dp2[i - 1]
for i in range(H):
	if r1 > dp1[i] + dp2[i]:
		r1 = dp1[i] + dp2[i]
		r2 = 1
	elif r1 == dp1[i] + dp2[i]:
		r2 += 1
print(r1, r2)
