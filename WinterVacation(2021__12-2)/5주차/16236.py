import copy
import sys
r = sys.stdin.readline

# 물고기가 있는지 없는지 판단
def search():
    cnt = 0
    tmp_size = sharkSize
    if sharkSize > 6:
        tmp_size = 6
    for i in range(0, tmp_size):
        if fish[i] > 0:
            cnt += fish[i]

    return cnt

# 이동가능한 좌표인지 판단
def validation(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True

def bfs():
    queue = []

    queue.append([x, y, 0])
    copyArr = copy.deepcopy(space)

    result = 0
    min_pos = [N, N, 40]
    while(len(queue) > 0):
        cx, cy, depth = queue.pop(0)
        if space[cx][cy] > 0 and space[cx][cy] < sharkSize+1:
            if min_pos[2] > depth:
                min_pos[0] = cx
                min_pos[1] = cy
                min_pos[2] = depth
            elif min_pos[2] == depth:
                if min_pos[0] > cx:
                    min_pos[0] = cx
                    min_pos[1] = cy
                    min_pos[2] = depth
                elif min_pos[0] == cx:
                    if min_pos[1] > cy:
                        min_pos[0] = cx
                        min_pos[1] = cy
                        min_pos[2] = depth
        for i in range(4):
            tmpx = cx + moveX[i]
            tmpy = cy + moveY[i]
            if validation(tmpx, tmpy) and copyArr[tmpx][tmpy] != 9 and space[tmpx][tmpy] <= sharkSize+1:
                queue.append([tmpx, tmpy, depth+1])
                copyArr[tmpx][tmpy] = 9

    if min_pos[2] == 40:
        return -1, -1, 40
    space[x][y] = 0
    fish[space[min_pos[0]][min_pos[1]] - 1] -= 1
    space[min_pos[0]][min_pos[1]] = 9
    return min_pos[0], min_pos[1], min_pos[2]

N = int(r())
fish = [0 for row in range(6)]
space = []

# 아기상어 위치를 담을 변수
x = 0
y = 0

for i in range(N):
    arr = list(map(int, r().split()))
    for j in range(N):
        if arr[j] == 0:
            continue
        elif arr[j] == 9:
            x = i
            y = j
        else:
            fish[arr[j]-1] += 1
    space.append(arr)


# 결과 이동시간(초)
second = 0
# 아기상어 사이즈
sharkSize = 1
# 물고기를 몇마리 먹었는지 세는 변수
food = -1
# 상어가 이동 가능한 위치
moveX = [0, 1, 0, -1]
moveY = [-1, 0, 1, 0]

num = search()
while(num > 0):
    if num == 1:
        tmp_size = sharkSize
        for i in range(N):
            for j in range(N):
                if space[i][j] > 0 and space[i][j] < tmp_size+1:
                    #second += abs(i - x)
                    #second += abs(j - y)
                    #fish[space[i][j] - 1] -= 1
                    #space[x][y] = 0
                    #space[i][j] = 9
                    tx, ty, cnt = bfs()
                    if cnt == 40:
                        break;
                    x = tx
                    y = ty
                    food += 1
                    second += cnt
                    if food == sharkSize:
                        food = -1
                        sharkSize += 1
                    #x = i
                    #y = j
                    num = search()
    else:
        tx, ty, cnt = bfs()
        if cnt == 40:
            break;
        x = tx
        y = ty
        second += cnt
        food += 1
        if food == sharkSize:
            food = -1
            sharkSize += 1
        num = search()

# 먹을 수 있는 물고기가 하나밖에 없을 때, 좌표끼리 차이를 구하는게 아니라
# 몸집이 상어보다 큰 녀석이 있으면 지나갈 수가 없는 것 까지 계산을 해야한다.

# 먹을 수 있는 물고기는 존재하지만 더 큰 물고기들이 감싸고 있어서
# 먹을 수 없는 경우도 생각해야한다.

# 시간초과 해결해야됨...
print(second, end='')