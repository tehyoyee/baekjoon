
from collections import defaultdict
visit = []

def dfs(cur, folders, files, selected, excepted):
	result = 0
	flag = 0
	print(cur)
	for i in range(len(folders)):
		if folders[i][1] == cur:
			flag = 1
			if folders[i][0] not in visit:
				visit.append(folders[i][0])
				result += dfs(folders[i][0], folders, files, selected, excepted)
	if flag == 0:
		for i in range(len(files)):
			if files[i][2] == cur:
				if files[i][0] not in excepted:
					if files[i][1][-2:] == "KB":
						print(int(files[i][1][:-2]))
						result += (int(files[i][1][:-2]) * 1024)
					else:
						print(int(files[i][1][:-1]))
						result += int(files[i][1][:-1])
	return result



def solution(folders, files, selected, excepted):
	result = 0

	for candi in selected:
		if candi not in visit:
			visit.append(candi)
			result += dfs(candi, folders, files, selected, excepted)
	return result

folders = [["animal", "root"], ["fruit", "root"]]
files = [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["apple", "4B", "fruit"]]
selected = ["animal"]
excepted = ["apple"]
print(solution(folders, files, selected, excepted))

folders = [["food", "root"], ["meat", "food"], ["fruit", "food"], ["animal", "root"]]
files = [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["fork", "1KB", "meat"], ["beef", "8KB", "meat"], ["apple", "4B", "fruit"], ["fire", "83B", "root"]]

selected = ["root", "meat"]
excepted = ["fork", "apple"]
print(solution(folders, files, selected, excepted))
