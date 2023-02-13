# 1107.py
# 23.02.13. 19:00 ~

# target = int(input())
# target_lst = list(map(int, str(target)))
# target_len = len(str(target))
# m = int(input())
# candi = []
# # button = str(list(set(chr(p) for p in range(48, 58)) - set(input().split())))
# if m == 0:
#     button = sorted(list(x for x in range(0, 9)))
# else:
#     button = sorted(list(set(x for x in range(0, 9)) - set(map(int, input().split()))))

# def bfs(target_len):
#     q = [[0, 0]]
#     while q:
#         v, l = q.pop(0)
#         if l == target_len:
#             print(v, l)
#             candi.append(v)
#         else:
#             for i in range(int(target_lst[l]), 10):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
#             for i in range(int(target_lst[l]) - 1, -1, -1):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
#             for i in range(9, -1, -1):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
# print(list(map(int, str(target))))
# bfs(target_len)
# if button[0] == 0:
#     tmp = button[1]
# else:
#     tmp = button[0]
# for i in range(target_len):
#     tmp = tmp * 10 + button[0]
# candi.append(tmp)
# result = 1000000000
# print(candi)
# for v in candi:
#     if abs(v - target) < abs(result - target):
#         result = v
#         print("result ", result)
# print(target-result)
# print(min(abs(target - 100), len(str(result)) + abs(target - result)))


    

# target = int(input())
# target_lst = list(map(int, str(target)))
# target_len = len(str(target))
# m = int(input())
# candi = []
# if m == 0:
#     button = sorted(list(x for x in range(0, 10)))
# else:
#     button = sorted(list(set(x for x in range(0, 10)) - set(map(int, input().split()))))
# def bfs(target_len):
#     q = [[0, 0]]
#     while q:
#         v, l = q.pop(0)
#         if l == target_len:
#             candi.append(v)
#         else:
#             for i in range(int(target_lst[l]), 10):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
#             for i in range(int(target_lst[l]) - 1, -1, -1):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
#             for i in range(9, -1, -1):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
# bfs(target_len)
# if len(button) > 0:
#     if len(button) >= 2 and button[0] == 0:
#         tmp1 = button[1]
#     else:
#         tmp1 = button[0]
#     tmp2 = 0
#     for _ in range(target_len):
#         tmp1 = tmp1 * 10 + button[0]
#         tmp2 = tmp2 * 10 + button[-1]
#     candi.append(tmp1)
#     candi.append(tmp2)

# result = 1000000000
# print(candi)
# for v in candi:
#     if abs(v - target) < abs(result - target):
#         result = v
# print(min(abs(target - 100), len(str(result)) + abs(target - result)))


# target = int(input())
# target_lst = list(map(int, str(target)))
# target_len = len(str(target))
# m = int(input())
# candi = []
# if m == 0:
#     button = sorted(list(x for x in range(0, 10)))
# else:
#     button = sorted(list(set(x for x in range(0, 10)) - set(map(int, input().split()))))
# def bfs(target_len):
#     q = [[0, 1]]
#     for i in range(int(target_lst[0]), 10):
#         if i in button:
#             q.append([i, 1])
#             break
#     for i in range(int(target_lst[0]) - 1, -1, -1):
#         if i in button:
#             q.append([i, 1])
#             break
#     print(q)
#     while q:
#         v, l = q.pop(0)
#         if l == target_len:
#             candi.append(v)
#         else:
#             for i in range(int(target_lst[0]), 10):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
#             for i in range(int(target_lst[0]) - 1, -1, -1):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
#             for i in range(9, -1, -1):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
#             for i in range(10):
#                 if i in button:
#                     q.append([10 * v + i, l + 1])
#                     break
# bfs(target_len)
# if len(button) > 0:
#     if len(button) >= 2 and button[0] == 0:
#         tmp1 = button[1]
#     else:
#         tmp1 = button[0]
#     tmp2 = 0
#     for _ in range(target_len):
#         tmp1 = tmp1 * 10 + button[0]
#         tmp2 = tmp2 * 10 + button[-1]
#     candi.append(tmp1)
#     candi.append(tmp2)

# result = 1000000000
# # print(candi)
# for v in candi:
#     if abs(v - target) < abs(result - target):
#         result = v
# print(min(abs(target - 100), len(str(result)) + abs(target - result)))



target = int(input())
target_lst = list(map(int, str(target)))
target_len = len(str(target))
m = int(input())
candi = []
if m == 0:
    button = sorted(list(x for x in range(0, 10)))
else:
    button = sorted(list(set(x for x in range(0, 10)) - set(map(int, input().split()))))



def bfs(target_len):
    q = [[0, 1], [0, 0], [0, -1]]
    while q:
        v, l = q.pop(0)
        if l >= target_len:
            candi.append(v)
        else:
            print(v, l)
            for x in button:
                if int(x) in button:
                    q.append([10 * v + int(x), l + 1])
bfs(target_len)

result = 1000000000
if button[0] != 0:
    while candi[0] == 0:
        candi.pop(0)
# print(candi)
for v in candi:
    if abs(v - target) < abs(result - target):
        result = v
print(min(abs(target - 100), len(str(result)) + abs(target - result)))