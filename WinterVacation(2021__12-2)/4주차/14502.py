# 파이썬에서는 시간초과
# pypy로 채점하면 정답으로 인정
# 최적화가 필요함

import copy
import sys
r = sys.stdin.readline

def validate(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    else:
        return True

def bfs():
    queue = []
    copyArr = copy.deepcopy(array)
    for i in range(N):
        for j in range(M):
            if copyArr[i][j] == 2:
                queue.append([i, j])

    while len(queue) > 0:
        temp = queue.pop(0)
        x = temp[0]
        y = temp[1]

        for i in range(4):
            tx = x + movex[i]
            ty = y + movey[i]

            if not validate(tx, ty):
                continue
            elif copyArr[tx][ty] == 0:
                copyArr[tx][ty] = 2
                queue.append([tx, ty])

    global result
    cnt = 0
    for i in range(N):
        cnt += copyArr[i].count(0)

    result = max(result, cnt)

def Wall(depth):
    if depth == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                array[i][j] = 1
                Wall(depth+1)
                array[i][j] = 0


N, M = r().split(" ")
N = int(N)
M = int(M)

array = []
movex = [0, 1, 0, -1]
movey = [-1, 0, 1, 0]

result = 0

for i in range(N):
    array.append(list(map(int, r().split())))

Wall(0)

print(result, end='')