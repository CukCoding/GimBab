import sys

r = sys.stdin.readline


def validate(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    else:
        return True


# 세로 N , 가로 M
N, M = list(map(int, r().split()))

# 로봇의 초기 위치, 바라보는 방향 d
rx, ry, d = list(map(int, r().split()))
queue = []
# 청소횟수 : cnt
cnt = 0
queue.append([rx, ry, d])
# 북쪽 : 0, 동쪽 : 1, 남쪽 : 2, 서쪽 : 3
move = [[-1, 0], [0, 1], [1, 0], [0, -1]]

array = []
for i in range(N):
    input = list(map(int, r().split()))
    array.append(input)

# 탐색
while len(queue) > 0:

    cx, cy, di = queue.pop(0)
    chk = 0

    if array[cx][cy] == 0:
        array[cx][cy] = 2
        cnt += 1

    for i in range(4):
        di = (di + 3) % 4
        m = move[di]
        tx = cx + m[0]
        ty = cy + m[1]
        if validate(tx, ty) and array[tx][ty] == 0:
            chk = 1
            queue.append([tx, ty, di])
            break

    if chk == 0:
        # 네방향 모두 청소가 이미 되어있는 경우
        back = (di + 2) % 4
        bx = cx + move[back][0]
        by = cy + move[back][1]
        if validate(bx, by) and array[bx][by] != 1:
            queue.append([bx, by, di])
        else:
            break
print(cnt, end='')
