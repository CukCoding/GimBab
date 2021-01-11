'''
    필수 조건 : 체스판은 딱 두 종류!!
    하나는 0,0 지점이 하얀색으로 시작하거나
    0,0 지점이 검은색으로 시작하는
    8*8 크기!

    그래서 하얀색으로 시작하는 체스판 1개랑 검정색으로 시작하는 체스판 1개를 배열에 저장해서
    8*8 크기로 자른 체스판이랑 다른거 갯수를 측정, 그 중 가장 작은 것을 출력하는 형태

    ex) 가로가 10칸이면 8개로 3번쪼개기 가능 1~8 / 2~9 / 3~10
       즉, X칸이면 8개로 X-7번으로 쪼개는 것이 가능하다.

    그래서 함수로 넘겨줄때 for문 i, j의 범위는 입력받은 가로, 세로에서 -7만큼 한 갯수로 이중 포문을 작동

    result 의 초기값이 2501인 이유는 가로 세로 각각 최댓값이 50이므로
    일치하지 않는 경우가 50 * 50 한 2500 보다 1개 더 많아야지 최솟값을 정확하게 측정가능
'''

blackChess = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

whiteChess = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
              ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

def whiteboard(x, y) :
    cnt = 0
    for i in range(0, 8) :
        for j in range(0, 8) :
            if matrix[x+i][y+j] != whiteChess[i][j] :
                cnt += 1
    return cnt

def blackboard(x, y) :
    cnt = 0
    for i in range(0, 8) :
        for j in range(0, 8) :
            if matrix[x+i][y+j] != blackChess[i][j] :
                cnt += 1
    return cnt


hei, wid = input().split()
wid = int(wid)
hei = int(hei)
result = 2501

matrix = [list(map(str, input())) for _ in range(hei)]

for i in range(0, hei-7) :
    for j in range(0, wid-7) :
        tmp = min(whiteboard(i, j), blackboard(i, j))
        if tmp < result :
            result = tmp

print(result)