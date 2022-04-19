# 10809 py

arr = [-1] * 26
str = input()
for i in range(len(str)):
    if (arr[ord(str[i]) - ord('a')] == -1):
        arr[ord(str[i]) - ord('a')] = i
for arr in arr:
    print(arr, end = " ")

