'''
    시간초과 나면 큐로 풀려고 했으나, list 만 사용해도 해결됨...
    원리는 너비탐색이고, 처음 배추밭을 0,0부터 시작해서 1을 만나는 지점에서 너비탐색을 하게 될때마다 카운트를 하면
    필요한 배추벌레 마리수를 구할 수 있다.

    너비탐색을 실시할때는 거쳐간 좌표는 1 -> 0으로 값을 바꿔주면서 해당 좌표를 큐에 집어넣고
    큐에서 좌표를 뽑아와서는 동서남북 칸에 1이 있는지, 그 칸이 배추 밭 안의 칸인지를 동시 조건으로 체크하고
    그 칸이 조건에 맞으면 다시 그 칸의 값을 1 -> 0으로 바꿔주고 큐에 넣어주는 형태로 실시해준다.
'''
import sys
from queue import Queue
r = sys.stdin.readline

moveX = [-1, 0, 1, 0] #상하좌우 탐색을 위해서 x, y로 이동가능한 좌표를 리스트에 저장해 놓앗다
moveY = [0, -1, 0, 1]

def check(x, y, wid, hei) : #해당 칸이 배추밭 이내의 칸인지 범위를 벗어나는지 탐색해준다.
    if x < wid and y < hei and x >= 0 and y >= 0 :
        return 1
    else :
        return 0

def bfs(cx, cy, wid, hei) :
    #q = Queue()
    #q.put([cx, cy])
    q = []
    q.append([cx, cy])
    while len(q) > 0 :
        x, y = q[0]
        del q[0]
        for i in range(4) :
            nx = x + moveX[i]
            ny = y + moveY[i]
            if check(nx, ny, wid, hei) == 1 and land[nx][ny] == 1:
                land[nx][ny] = 0
                q.append([nx, ny])
                #q.put([nx, ny])

T = int(r())
result = []

for i in range(T) :
    cnt = 0
    temp = list(map(int, r().split()))
    land = [[0 for _ in range(temp[0])] for _ in range(temp[1])]

    for j in range(temp[2]) :
        xy = list(map(int, r().split()))
        land[xy[1]][xy[0]] = 1

    for j in range(temp[1]) :
        for k in range(temp[0]) :
            if land[j][k] == 1 :
                land[j][k] = 0
                bfs(j, k, temp[1], temp[0])
                cnt += 1

    result.append(cnt)

for i in result :
    print(i)