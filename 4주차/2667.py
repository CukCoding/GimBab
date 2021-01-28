'''
    원리 : map함수에 입력을 받고, copy배열로 똑같은 크기를 만든다.
    처음에 단지를 묶기 시작하는 조건은 map함수 값이 1이고 copy배열에 값이 0인 좌표부터 시작!
    가로 세로로 단지를 탐색할 수 있는 범위는 x,y값이 각각 4개씩 moveX, moveY에 저장

    for문으로 각각의 좌표가 배열 안에 존재하는 좌표인지, 그리고 map에서 1을 가지고 잇는지, 마지막으로
    copy에서 아직 단지로 묶여지지 않은 좌표인지(=0) 확인

    조건을 만족한다면 visit[]배열에 푸쉬한다. 그런식으로 너비탐색 계속
    solve()함수에서 몇번의 단지를 형성하게 되는지 cnt값을 가지고 잇다가 리턴해주고
    각각의 단지수는 createGroup()에서 visit배열이 빌때까지 탐색하고 그 숫자만큼 저장해준다.

    현재 sort를 내장 sort함수로 하고 있는데, 곧 직접 구현 sort로 수정할 예정
'''
from sys import stdin
def check(x, y) :
    if x >= 0 and y >= 0 and x < size and y < size :
        return 1
    else :
        return 0
def createGroup(x, y, cnt) :
    apart = 1
    visit.append([x, y])
    copy[x][y] = cnt
    while len(visit) > 0 :
        cx = visit[0][0]
        cy = visit[0][1]
        del visit[0]
        for i in range(4) :
            nx = cx + moveX[i]
            ny = cy + moveY[i]
            if check(nx, ny) == 1 and map[nx][ny] == 1 and copy[nx][ny] == 0 :
                copy[nx][ny] = cnt
                visit.append([nx, ny])
                apart += 1

    result.append(apart)


def solve() :
    cnt = 1
    for i in range(size) :
        for j in range(size) :
            if map[i][j] == 1 and copy[i][j] == 0 :
                createGroup(i, j, cnt)
                cnt += 1
    return cnt - 1

size = int(stdin.readline())
copy = [[0 for _ in range(size)] for _ in range(size)]
moveX = [-1, 0, 0, 1]
moveY = [0, -1, 1, 0]
result = []
visit = []

map = [list(map(int, stdin.readline().strip())) for _ in range(size)]

total = solve()
result.sort()
print(total)
for i in range(total) :
    print(result[i])