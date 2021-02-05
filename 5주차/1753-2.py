'''
    시간초과 코드...
'''
from sys import stdin
import heapq

def dijkstra(k) :
    heapq.heappush(heap, (0, k)) #시작정점과 시작정점까지의 가중치(0)을 힙에 넣고 시작한다

    while heap : #힙이 빌때까지
        minW = heapq.heappop(heap) #힙의 우선순위제일 높은것을 pop한다
        #minW[0]은 해당 하는 정점까지의 최소거리
        #minW[1]은 해당 하는 정점
        if result[minW[1]] >= minW[0] : #시작점에서 minW[1]까지의 거리보다 큐에 들어가있는 값이 더 작으면 최솟값을
                                        #변경해야할 필요가 있다
            for i in range(v) :
                if matrix[minW[1]][i] > 0 and matrix[minW[1]][i] < 11: #가져온 점에서 다른 정점으로의 가는 길이 있다면
                    temp = minW[0] + matrix[minW[1]][i] #가져온 정점까지의 거리 + 그 점에서 다른 정점으로의 거리를 더해주고
                    if result[i] > temp : #이미 저장되어있는 거리값과 비교해서 최솟값의 변경이 필요하면
                        result[i] = temp #result에 temp를 넣음으로써 변경해주고
                        heapq.heappush(heap, (temp, i)) #해당 정점까지의 최단거리를 힙에 넣는다

heap = [] #힙큐로 쓸 리스트 선언
v, e = stdin.readline().split()
v = int(v) #정점 갯수
e = int(e) #입력되는 선 갯수

matrix = []
for i in range(v) :
    a=[]
    for j in range(v) :
        if i == j : #자기 자신으로 향하는 선은 가중치를 0으로 설정한다.. ex) 0,0 = 0 / 1,1 = 0 ...
            a.append(0)
        else :
            a. append(11) #그외의 가중치는 가중치의 최댓값인 10 + 1한 11을 넣는다
    matrix.append(a)

k = int(stdin.readline()) #시작정점

for i in range(e) :
    stroke = list(map(int, stdin.readline().split()))
    matrix[stroke[0] - 1][stroke[1] - 1] = stroke[2] #입력받은 수를 토대로 가중치를 2차원 배열에 추가

result = [] #가중치 배열 초기화
for i in range(v) :
    if i == k - 1 :
        result.append(0) #시작정점 자기자신으로 향하는 선은 가중치 0 할당
    else :
        result.append(11) #나머지는 최댓값으로 초기화

dijkstra(k - 1) # -1해주는 이유 배열은 0부터 시작이어서

for i in result :
    if i == 11 :
        print("INF")
    else :
        print(i)