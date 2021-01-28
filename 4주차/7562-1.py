'''
    두번째 코드 : 따로 Queue를 사용하지 않고 리스트에 append와 del을 이용해서 다음에 탐색할 좌표들을 저장한다.
    시간 단축 : 내가 원하는 좌표에 도달시 clear를 이용해서 다음 탐색해야할 좌표를 완전히 비우면
               while문 조건에 의해서 탈출되며 Solve()함수가 종료된다.
'''
from sys import stdin

def check(x, y) :
    if x >= 0 and x < pos[0] and y >= 0 and y < pos[0] :
        return 1
    else :
        return 0

def solve() :
    x = pos[1][0]
    y = pos[1][1]
    chess[x][y] = 1
    visit.append([x, y])
    while len(visit) > 0 :
        x = visit[0][0]
        y = visit[0][1]
        del visit[0]
        for i in range(8) :
            tx = x + moveX[i]
            ty = y + moveY[i]
            if check(tx, ty) == 1 and chess[tx][ty] == 0 :
                chess[tx][ty] = chess[x][y] + 1
                visit.append([tx, ty])
                if tx == pos[2][0] and ty == pos[2][1] :
                    visit.clear()
                    break
moveX = [-2, -1, 1, 2, -2, -1, 1, 2]
moveY = [-1, -2, -2, -1, 1, 2, 2, 1]
visit = []
result = []
testcase = int(stdin.readline())

for i in range(testcase) :
    size = int(stdin.readline())
    pos = []
    chess = [[0 for _ in range(size)] for _ in range(size)]
    pos.append(size)
    for j in range(2) :
        pos.append(list(map(int, stdin.readline().split())))

    if pos[1][0] == pos[2][0] and pos[1][1] == pos[2][1] :
        result.append(0)

    else :
        solve()
        result.append(chess[pos[2][0]][pos[2][1]] - 1)

for i in result :
    print(i)