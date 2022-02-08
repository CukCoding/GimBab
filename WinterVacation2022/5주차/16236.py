import sys
r = sys.stdin.readline

def search():
    chk = 0
    for i in range(N):
        for j in range(N):
            if space[i][j] > 0 and space[i][j] < sharkSize:
                chk = 1
                break
    if chk:
        return True
    else:
        return False

def validate(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True

def bfs(x, y):
    queue = []
    queue.append([x, y, 0])
    #방문한 노드 체크
    visit[x][y] = 1

    #최단거리 x, y, 걸린시간을 가지고 있는 배열
    minpos = [21, 21, 401]

    while len(queue) > 0:
        cx, cy, dep = queue.pop(0)
        if space[cx][cy] > 0 and space[cx][cy] < sharkSize:
            # 먹을 수 있는 물고기일 경우
            if minpos[2] > dep:
                minpos[0] = cx
                minpos[1] = cy
                minpos[2] = dep
            elif minpos[2] == dep:
                # 위에 있는 녀석이 최소
                if minpos[0] > cx:
                    minpos[0] = cx
                    minpos[1] = cy
                    minpos[2] = dep
                elif minpos[0] == cx:
                    # 가장 왼쪽에 있는 녀석이 최소
                    if minpos[1] > cy:
                        minpos[0] = cx
                        minpos[1] = cy
                        minpos[2] = dep

        # bfs 중지 조건, 먹을 수 있는 물고기가 이미 나온경우 : depth가 초기값이 아니면 더이상 bfs를 탐색할 필요 없음
        if minpos[2] == 401:
            for i in range(4):
                tx = cx + moveX[i]
                ty = cy + moveY[i]
                if validate(tx, ty) and visit[tx][ty] == 0 and space[tx][ty] <= sharkSize:
                    queue.append([tx, ty, dep+1])
                    visit[tx][ty] = 1

    for i in range(N):
        for j in range(N):
            # visit 배열 초기화
            visit[i][j] = 0

    if minpos[2] == 401:
        # 먹을 수 있는 물고기가 있는데 상어가 접근 불가능
        return -1, -1, -1
    else:
        # 상어위치 변경
        space[x][y] = 0
        space[minpos[0]][minpos[1]] = 9
        # print(minpos[2])
        return minpos[0], minpos[1], minpos[2]

N = int(r())
# 방문한 노드인지 아닌지 판단하기 위해 visit배열 만듬
visit = [[0 for row in range(N)] for col in range(N)]
sharkSize = 2

space = []
for i in range(N):
    tmp = list(map(int, r().split()))
    space.append(tmp)

# 상어의 초기위치 찾기
sx = 0
sy = 1
moveX = [0, 1, 0, -1]
moveY = [-1, 0, 1, 0]
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            sx = i
            sy = j

# 상어가 이동하는데 걸린시간
second = 0
# 상어가 먹은 먹이의 수
fish = 0
while search():
    mx, my, result = bfs(sx, sy)
    if result == -1:
        break
    else:
        sx = mx
        sy = my
        second += result
        fish += 1
        if fish == sharkSize:
            # 물고기를 사이즈 만큼 먹은 경우 해야 할 일 먹은 물고기 수 초기화 + 상어 사이즈 1증가
            fish = 0
            sharkSize += 1

        # for i in space:
        #     print(i)
        # print()

print(second, end='')