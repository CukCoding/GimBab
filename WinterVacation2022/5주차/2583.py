import sys
r = sys.stdin.readline

def validate(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    else:
        return True

def bfs(x, y):
    queue = []
    queue.append([x, y])
    array[x][y] = 1
    cnt = 1
    while(len(queue) > 0):
        tx, ty = queue.pop(0)

        for i in range(4):
            cx = tx + searchX[i]
            cy = ty + searchY[i]
            if validate(cx, cy) and array[cx][cy] == 0:
                queue.append([cx, cy])
                array[cx][cy] = 1
                cnt += 1

    return cnt

# M = 세로 , N = 가로
M, N, K = list(map(int, r().split()))

array = [[0 for row in range(N)] for col in range(M)]

for i in range(K):
    dx, dy, ux, uy = list(map(int, r().split()))
    # 컴퓨터 array 좌표로 변경하면 x는 그대로 y는 반대로 M - y
    for x in range(M - uy, M - dy):
        for y in range(dx, ux):
            array[x][y] = 2

result = []
searchX = [-1, 0, 1, 0]
searchY = [0, 1, 0, -1]
part = 0
for i in range(M):
    for j in range(N):
        if array[i][j] == 0:
            part += 1
            result.append(bfs(i, j))

result.sort()
print(part)
for i in range(len(result)):
    print(result[i], end='')
    if i != len(result) - 1:
        print("", end=' ')