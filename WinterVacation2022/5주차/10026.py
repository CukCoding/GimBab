import copy
import sys
r = sys.stdin.readline

def validate(x, y):
    if x < 0 or x >=  N or y < 0 or y >= N:
        return False
    else:
        return True

def bfs(x, y, carr):
    queue = []
    queue.append([x, y])
    char = carr[x][y]
    carr[x][y] = 0

    while (len(queue) > 0):
        tx, ty = queue.pop(0)
        for i in range(4):
            cx = tx + moveX[i]
            cy = ty + moveY[i]
            if validate(cx, cy) and carr[cx][cy] == char:
                queue.append([cx, cy])
                carr[cx][cy] = 0

N = int(r())
# 일반인이 보는 세상
space1 = []
# 적록색약이 보는 세상
space2 = []
for i in range(N):
    arr = list(r().strip())
    space1.append(arr)

space2 = copy.deepcopy(space1)
for i in range(N):
    for j in range(N):
        if space2[i][j] == 'R':
            space2[i][j] = 'G'

# 일반인 구역
cnt1 = 0
# 적록색약 구역
cnt2 = 0

moveX = [0, 1, 0, -1]
moveY = [-1, 0, 1, 0]

for i in range(N):
    for j in range(N):
        if space1[i][j] == 'R' or space1[i][j] == 'G' or space1[i][j] == 'B':
            bfs(i, j, space1)
            cnt1 += 1
        if space2[i][j] == 'G' or space2[i][j] == 'B':
            bfs(i, j, space2)
            cnt2 += 1

print(cnt1, cnt2, end='')