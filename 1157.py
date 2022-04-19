# 1157 py

str = input().upper()
unique_words = list(set(str))
cnt = []
for x in unique_words:
   cnt.append(str.count(x))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    max_index = cnt.index(max(cnt))
    print(unique_words[max_index])