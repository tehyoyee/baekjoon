

def findRoot(x):
	if x != root[x]:
		root[x] = findRoot(root[x])
	return root[x]

def solution(n, network, repair):
	repair.sort(key=lambda x:x[2])
	result = 0

	root = [i for i in range(n + 1)]

	for s, e in network:
		sRoot = findRoot(s)
		eRoot = findRoot(e)
		if sRoot != eRoot:
			if sRoot > eRoot:
				root[sRoot] = eRoot
		else:
			root[eRoot] = sRoot

	print(root)





n = 4
network = [[1, 2], [3, 5], [4, 2], [5, 6]]
repair = [[3, 2, 10], [5, 4, 15]]
