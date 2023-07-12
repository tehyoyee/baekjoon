# 2749.py
# 23.07.12. 15:35 ~ x 피사노주기

from collections import deque

N = int(input())
lst = deque([])
lst.append(0)
lst.append(1)
lst.append(1)

M = 15 * 10**5

N = N%M

for i in range(2, N):
	lst.append((lst[1] + lst[2]) % 1000000)
	lst.popleft()
print(lst[-1])