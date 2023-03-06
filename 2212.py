# 2212.py
# 23.03.06. 17:00 고민을 오래했지만, 정답을 찾지 못하였다. 이분탐색이 아니었다니...

N = int(input())
K = int(input())
graph = list(map(int, input().split()))
graph.sort()
if N == K:
	print(0)
	exit()
for i in range(1, N):
    graph[i - 1] = graph[i] - graph[i - 1]
graph.pop()
graph.sort()
print(sum(graph[:N - K]))