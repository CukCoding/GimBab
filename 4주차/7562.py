'''
    원리 : BFS // 시간초과
    파이썬 Queue()는 put, get 두가지의 메소드로 작동
    첫번째 좌표를 queue에 넣는 것으로 시작
    큐에서 좌표를 꺼내서 나이트가 이동할 수 있는 범위들을 하나하나 체크(체스판 안의 좌표인지)
    그러고 나서 이동할 수 있는 곳이라면 몇번째로 이동가능한 좌표인지 숫자를 마킹하고 큐에 넣는다

    탐색하다가 똑같은 좌표에 여러번 도달할 수 있는데,
    예를들어 2번째로 도착할 수 있는 좌표가 5번째 이동으로도 도착할수 있다면, 그럴때는 5라는 숫자를 저장하면 안된다
    왜냐하면 최솟값을 찾아야하므로..
    그래서 조건문에서 해당 칸이 0일 경우(즉, 방문을 한번도 하지않은 좌표)에만 값을 넣어주는형식이다.

    마지막 결과문에서 내가 원하는 도착지점의 좌표에 들어가있는 숫자를 프린트 하면
    최솟값을 얻을 수 있다.
'''
from sys import stdin
from queue import Queue

def check(x, y) :
    if x >= 0 and x < pos[0] and y >= 0 and y < pos[0] :
        return 1
    else :
        return 0

def solve() :
    chess[pos[1][0]][pos[1][1]] = 1
    visit.put([pos[1][0], pos[1][1]])

    while visit.qsize() > 0 :
        x, y = visit.get()
        for i in range(8) :
            tx = x + moveX[i]
            ty = y + moveY[i]
            if check(tx, ty) == 1 and chess[tx][ty] == 0 :
                chess[tx][ty] = chess[x][y] + 1
                visit.put([tx,ty])


moveX = [-2, -1, 1, 2, -2, -1, 1, 2]
moveY = [-1, -2, -2, -1, 1, 2, 2, 1]
visit = Queue()
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
