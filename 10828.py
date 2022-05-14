import sys
input = sys.stdin.readline

stack = []

def commaned_select(command):
    if "push" in command:
        number = (command.split())[1]
        stack.append(number)
    elif "pop" in command:
        if len(stack):
            print(stack.pop())
        else:
            print("-1")
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if len(stack):
            print("0")
        else:
            print("1")
    else:
        if len(stack):
            print(stack[-1])
        else:
            print("-1")
            
n = int(input())
for _ in range(n):
    command = input()
    commaned_select(command)