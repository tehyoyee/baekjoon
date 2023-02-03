# 12852.py
# 23.02.03. 10:17 ~

n = int(input())
p = []
visit = [100000] * 1000001

def bfs(i):
	q = [[i, 0, [i]]]
	while q:
		cur, cnt, path = q.pop(0)
		if cur == 1:
			print(cnt)
			for x in path:
				print(x, end=" ")
			break
		else:
			if cur % 3 == 0:
				tmp = cur // 3
				if visit[tmp] > cnt:
					visit[tmp] = cnt
					q.append([tmp, cnt + 1, path + [tmp]])
			if cur % 2 == 0:
				tmp = cur // 2
				if visit[tmp] > cnt:
					visit[tmp] = cnt
					q.append([tmp, cnt + 1, path + [tmp]])
			tmp = cur - 1
			if visit[tmp] > cnt:
				visit[tmp] = cnt
				q.append([tmp, cnt + 1, path + [tmp]])

bfs(n)