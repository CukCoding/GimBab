from sys import stdin
from collections import deque

num = int(stdin.readline())
arr = deque()
for i in range(1, num + 1) :
    arr.append(i)

while len(arr) > 1 :
    arr.popleft()
    temp = arr.popleft()
    arr.append(temp)

print(arr[0])