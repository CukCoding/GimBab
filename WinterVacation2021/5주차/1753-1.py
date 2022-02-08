'''
    메모리 초과 코드
'''
from sys import stdin

def dijkstra(startP) :
    visit = [True for _ in range(size)]
    visit[startP] = False
    cnt = 1

    while cnt < size :
        minW = 11
        nextNode = 0
        for i in range(size) :
            if visit[i] == True and visit[i] != -1:
                if w[startP][i] < minW :
                    minW = w[startP][i]
                    nextNode = i

        visit[nextNode] = False
        for j in range(size) :
            if j == startP or w[nextNode][j] == -1 :
                continue
            elif w[startP][j] == -1 :
                w[startP][j] = w[nextNode][j] + minW
            elif w[nextNode][j] + minW < w[startP][j] :
                w[startP][j] = w[nextNode][j] + minW

        cnt += 1

size, stroke = stdin.readline().split()
size = int(size)
stroke = int(stroke)

w = [[-1 for _ in range(size)] for _ in range(size)]

startP = int(stdin.readline())

for i in range(stroke) :
    inputW = list(map(int, stdin.readline().split()))
    w[inputW[0] - 1][inputW[1] - 1] = inputW[2]

for i in range(size) :
    w[i][i] = 0

dijkstra(startP - 1)

for i in range(size) :
    if w[startP - 1][i] == -1 :
        print("INF")
    else :
        print(w[startP - 1][i])