'''
    메모리 초과
'''
from sys import stdin
from collections import deque

def solve(start) :
    min[start] = 0 #자기 자신은 0으로 초기화
    q.append([start, 0]) #큐에 시작정점과 시작점까지의 거리 = 0을 넣어준다
    while q :
        pos, len = q.popleft() #큐에 들어간 점과 가중치를 가져온다
        for i in range(V) :
            if pos == i :
                continue
            elif matrix[pos][i] > 0 and matrix[pos][i] < 11 :
                temp = matrix[pos][i]
                if min[i] > len + temp :
                    min[i] = len + temp
                    q.append([i, len + matrix[pos][i]])


V, E = map(int, stdin.readline().split())
K = int(stdin.readline())

matrix = [[11 for col in range(V)] for row in range(V)]
q = deque()
min = [11 for _ in range(V)]

for i in range(E) :
    u,v,w = map(int, stdin.readline().split())
    matrix[u - 1][v - 1] = w


solve(K-1) #-1을 하는 이유는 배열 시작은 1이 아니라 0이라서

for i in min :
    if i == 11 :
        print("INF")
    else :
        print(i)