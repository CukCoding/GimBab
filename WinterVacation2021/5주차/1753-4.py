'''
    힙큐를 이용해서 통과..
    참고 한점 : 최댓값을 얼마나 크게 잡아야 하는지 몰라서 INF 값을 참고하였음..

    우선순위 큐쓰면 시간초과 안나는 이유 : 가중치가 적은 것부터 비교해서 최소거리 배열에 들어가기 때문에
    비교하고 작으면 큐에 넣는 과정이 줄어든다
'''
from sys import stdin
from heapq import heappop, heappush
INF = 1e9

def solve(start) :
    min = [INF for _ in range(V)]
    min[start] = 0 #자기 자신은 0으로 초기화
    heappush(q, (0, start)) #큐에 시작정점과 시작점까지의 거리 = 0을 넣어준다

    while q :
        l, p = heappop(q) #큐에 들어가 있는 점과 가중치를 가져온다 => 이 점을 기준으로 거리 계산을 시작

        for tp, tl in matrix[p] : #가져온 점에서 갈수있는 점들과 거리를 가져온다
            tl += l
            if min[tp] > tl : #지금 내가 있는 정점 l 까지의 거리 p + 갈수있는정점 tp 까지의 거리 tl 을 더한것이
                                   #최소거리 배열에 있는 저장되어있는 tp까지의 거리보다 작을경우
                min[tp] = tl
                heappush(q, (tl, tp)) #우선순위큐에 tp까지의 최소거리 p + tl 과 tp(정점) 을 넣는다

    return min


V, E = map(int, stdin.readline().split())
K = int(stdin.readline())

matrix = [[] for row in range(V)] #가중치를 저장하기 위한 이차원 리스트
q = [] #힙큐로 쓸 리스트 선언

for i in range(E) :
    u,v,w = map(int, stdin.readline().split())
    matrix[u - 1].append([v - 1, w]) #u점에서 갈수 있는 v점과 w거리를 배열에 넣는다


for i in solve(K-1) : #-1을 하는 이유는 배열 시작은 1이 아니라 0이라서
    if i == INF :
        print("INF")
    else :
        print(i)