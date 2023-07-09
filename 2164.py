# 2164.py
# 23.07.09. 17:27 ~ 17:29

from collections import deque

N = int(input())
lst = deque([i for i in range(1, N + 1)])

while len(lst) > 1:
	lst.popleft()
	lst.rotate(-1)
print(lst[0])