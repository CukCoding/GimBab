'''
    deque를 쓰는 이유는 양방향에서 데이터를 처리할 수 있기 때문에 시간복잡도가 O(1)로 아주 빠름
'''
from sys import stdin
from collections import deque

testCase = int(stdin.readline())
q = deque()
for i in range(testCase) :
    cmd = stdin.readline().split()
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(q) == 0 :
            print(-1)
        else :
            print(q.popleft())
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0 :
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(q) == 0 :
            print(-1)
        else :
            print(q[0])
    elif cmd[0] == 'back':
        if len(q) == 0 :
            print(-1)
        else :
            print(q[-1])
    else :
        print("Input MISS")