'''
    현재 런타임 에러
'''
from sys import stdin
from collections import deque

testCase = int(stdin.readline())

for i in range(testCase) :
    checkReverse = 0
    error = 0
    str = list(stdin.readline().strip())
    count = int(stdin.readline())
    arr = deque()
    temp = list(stdin.readline().strip())
    for i in range(1, (count * 2) + 1) :
        if i % 2 == 1 :
            arr.append(int(temp[i]))
    for i in  range(len(str)):
        if str[i] == 'R':
            if checkReverse == 0 :
                checkReverse = 1
            else :
                checkReverse = 0
        else :
            if len(arr) == 0 :
                print("error")
                error = 1
                break
            else :
                if checkReverse == 1 :
                    arr.pop()
                else :
                    arr.popleft()

    if error == 1 :
        continue

    elif checkReverse == 1 :
        print('[', end="")
        for j in range(len(arr) - 1, -1, -1) :
            if j == 0 :
                print(arr[j], end="")
            else :
                print(arr[j], end=",")
        print(']')

    else :
        print('[', end="")
        for j in range(len(arr)) :
            if j == count - 1 :
                print(arr[j], end="")
            else :
                print(arr[j], end=",")
        print(']')