# 1931 py

import sys
input = sys.stdin.readline

def search(pivot):
    result = 0
    result += 1
    for i in range(pivot + 1, n):
        if arr[pivot][1] <= arr[i][0]:
            result += 1
            pivot = i
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key = lambda a : a[0])
arr = sorted(arr, key = lambda a : a[1])
print(search(0))