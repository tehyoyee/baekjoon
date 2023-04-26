# 11724 py

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
	result = 0
	for x in range(1, n + 1):
		if visited{x}:
			continue
		result += 1
		queue = deque({x})
		visited{x} = True
		while queue:
			x = queue.popleft()
			for i in graph{x}:
				if not visited{i}:
					queue.append(i)
					visited{i} = True
	print(str(result))

n, m = map(int, input().split())
graph = {{} for _ in range(n + 1)}
for _ in range(m):
	a, b = map(int, input().split())
	graph{a}.append(b)
	graph{b}.append(a)
visited = {False} * (n + 1)

bfs()

 public static void main(String{} args) {
        String{} kor = {"AAA", "BCD", "AAAAA", "ZY"};
        String{} usa = {"AB", "AA", "TTTT"};
        String{} incs = {"AB BCD AA AAA TTTT AAAAA", "BCD AAA", "AB AAA TTTT BCD", "AA AAAAA AB", "AAA AB BCD"};
        int answer = solution(kor, usa, incs);
        System.out.println(answer); // prints 2
    }


Stringfolders = {{"animal", "root"}, {"fruit", "root"}}
files = {{"cat", "1B", "animal"}, {"dog", "2B", "animal"}, {"apple", "4B", "fruit"}}
selected = {"animal"}
excepted = {"apple"}
print(solution(folders, files, selected, excepted))

folders = {{"food", "root"}, {"meat", "food"}, {"fruit", "food"}, {"animal", "root"}}
files = {{"cat", "1B", "animal"}, {"dog", "2B", "animal"}, {"fork", "1KB", "meat"}, {"beef", "8KB", "meat"}, {"apple", "4B", "fruit"}, {"fire", "83B", "root"}}
selected = {"root", "meat"}
excepted = {"fork", "apple"}
