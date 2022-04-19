# 5622 py

str = input()
words = ['c=', 'c-', 'lj', 'nj', 'dz=', 'd-', 's=', 'z=']
for word in words:
    str = str.replace(word, '*')
print(len(str))