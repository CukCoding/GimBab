import sys
r = sys.stdin.readline

input = r()

stack = []
top = -1
chk = 0

for i in input:
    if chk == 1:
        break
    elif i == '(':
        stack.append('(')
        top += 1
    elif i == '[':
        stack.append('[')
        top += 1
    elif i == ')':
        temp = 0
        while True:
            if top == -1:
                chk = 1
                break
            else:
                left1 = stack.pop(top)
                top -= 1
                if left1 == '(':
                    if temp == 0:
                        temp = 2
                    else:
                        temp *= 2
                    break
                elif left1 == '[':
                    chk = 1
                    break
                else:
                    temp += left1
        stack.append(temp)
        top += 1
    elif i == ']':
        temp = 0
        while True:
            if top == -1:
                chk = 1
                break
            else:
                left2 = stack.pop(top)
                top -=1
                if left2 == '[':
                    if temp == 0:
                        temp = 3
                    else:
                        temp *= 3
                    break
                elif left2 == '(':
                    chk = 1
                    break
                else:
                    temp += left2
        stack.append(temp)
        top += 1

if chk == 1:
    print(0)
else:
    result = 0
    for i in stack:
        if i == '(' or i == ')' or i == '[' or i ==']':
            result = 0
            break
        result += i
    print(result)