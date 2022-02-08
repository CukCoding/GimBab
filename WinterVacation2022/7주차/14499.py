import sys
r = sys.stdin.readline

def validate(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    else:
        return True

def turn(command):
    temp = dice[2]
    if command == 1:
        # 동쪽 이동이면 북, 남 빼고 전부 변한다
        dice[2] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp
    elif command == 2:
        # 서쪽 이동이면 북, 남 빼고 전부 변한다
        dice[2] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp
    elif command == 3:
        # 북쪽 이동이면 동, 서 빼고 전부 변한다
        dice[2] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[0]
        dice[0] = temp
    elif command == 4:
        # 남쪽 이동이면 동, 서 빼고 전부 변한다
        dice[2] = dice[0]
        dice[0] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp

N, M, x, y, K = list(map(int, r().split()))

space = []
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
# 북, 서, 윗면, 동, 남, 밑면
dice = [0] * 6
# 조건 2: 주사위는 윗면이 1, 동쪽을 바라보는 방향이 3인 상태로
# 놓여져 있다.
for i in range(N):
    input = list(map(int, r().split()))
    space.append(input)

cmd = list(map(int, r().split()))

# 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4
move = [[0, 1], [0, -1], [-1, 0], [1, 0]]

for i in cmd:
    tx = x + move[i-1][0]
    ty = y + move[i-1][1]
    if validate(tx, ty):
        x = tx
        y = ty
        if space[tx][ty] == 0:
            turn(i)
            space[tx][ty] = dice[5]
        else:
            turn(i)
            dice[5] = space[tx][ty]
            space[tx][ty] = 0
        print(dice[2])