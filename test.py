import random
import math
import time
from collections import OrderedDict
import copy

def compareGrades(a, b):
	if str(a)[0] == str(b)[0]:
		return -1
	if a > b:
		return 1
	else:
		return 0

def compareHomes(a, b):
	aDist = a[0]**2 + a[1]**2
	bDist = b[0]**2 + b[1]**2
	if aDist == bDist:
		return -1
	if aDist > bDist:
		return 1
	else:
		return 0

def compareNames(a, b):
	if a < b:
		return a
	else:
		return b

names = []
grades = []
homes = []

for i in range(100):
	grades.append(round(random.random() * 1000 % 350 / 100 + 1.00, 2))
for i in range(100):
	tmp = ""
	for j in range(10):
		tmp += chr(int((random.random() * 100 % 25) + 97))
	names.append(tmp)
for i in range(100):
	tmp = [math.trunc(round(random.random() * 100)), math.trunc(round(random.random() * 100))]
	homes.append(tmp)

gradesCopy = copy.deepcopy(grades)

start = time.time()
rank = [1] * 100
for i in range(100):
	for j in range(i + 1, 100):
		tmp = compareGrades(grades[i], grades[j])
		if tmp == 1:
			rank[j] += 1
			continue
		elif tmp == 0:
			rank[i] += 1
			continue
		tmp = compareHomes(homes[i], homes[j])
		if tmp == 1:
			rank[j] += 1
			continue
		elif tmp == 0:
			rank[i] += 1
			continue
		tmp = compareNames(names[i], names[j])
		if tmp == 1:
			rank[j] += 1
		else:
			rank[i] += 1
end = time.time()
time2 = round(end-start, 5)
result2 = rank


start = time.time()
answer = []
dic = OrderedDict()
for name in names:
	dic[name] = 0
for i, (x, y) in enumerate(homes):
	homes[i] = x*x + y*y
for i, grade in enumerate(grades):
	grades[i] = int(grade)
lst = list(zip(grades, homes, names))
lst.sort(key=lambda x : (-x[0], -x[1], x[2]))
for i, (grade, home, name) in enumerate(lst):
	dic[name] = i + 1
for rank in dic.values():
	answer.append(rank)

end = time.time()
time1 = round(end-start, 5)

result1 = answer

print(time1, time2)

# for i in range(10):
# 	print(result1[i], result2[i], gradesCopy[i], homes[i], names[i])