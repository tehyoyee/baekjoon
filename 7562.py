# 7562
# 17:50 - 18:16

import sys
input = sys.stdin.readline
from collections import deque

	# 11  10  8  7  5  4   2   1
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

def check_dir(cur_next, tar):
	if 

def to_target(cur_x, cur_y, tar_x, tar_y):
	q_x = deque()
	q_y = deque()
	q_x = cur_x
	q_y = cur_y
	while q_x:
		v_x = q_x
		v_y = q_y
		for k in range(8):
			if check_dir(v_x + dx[k], tar_x) and check_dir(v_y + dy[k])
			q_x.append(v_x + dx[k])
			q_y.append(v_y + dy[k])

def before_bfs():
	while abs(tar_x - cur_x) and abs(tar_x - cur_x) > 4:
		
		


n = int(input())
for _ in range(n):
	size = int(input())
	cur_x, cur_y = map(int, input().split())
	tar_x, tar_y = map(int, input().split())
