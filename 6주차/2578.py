import sys
r = sys.stdin.readline

def checkXY(num) : #해당 넘버의 x,y 좌표를 구하기 위한 함수
    for i in range(5) :
        for j in range(5) :
            if bingo[i][j] == num :
                return i, j
bingo = [list(map(int, r().split())) for _ in range(5)] #빙고 입력판 배열
call = [list(map(int, r().split())) for _ in range(5)] #사회자가 부르는 순서 배열
wid = [0 for _ in range(5)] #가로 행마다 채워들어갈때 갯수 체크
hei = [0 for _ in range(5)] #세로 열 마다 채워들어갈때 갯수 체크
leftUp = 0 #왼쪽 위 -> 오른쪽 아래 대각선 채워지는 갯수 체크
rightUp = 0 #왼쪽 아래 -> 오른쪽 위 대각선 채워지는 갯수 체크
cnt = 0 #줄이 완성될때마다 카운트

for i in range(5) :
    for j in range(5) :
        x, y = checkXY(call[i][j]) #똑같은 숫자를 빙고판에서 찾아서 x,y값 반환
        wid[x] += 1
        hei[y] += 1
        # 예를 들어 5라는 숫자가 2, 3에 들어가있으면, wid[2] 와 hei[3]의 카운트가 하나씩 플러스 된다

        if x == y: #왼쪽 위에서 오른쪽 아래 대각선에 해당되는 칸 확인
            leftUp += 1
            if leftUp == 5: # 5칸이 모두 차면 한줄 완성
                cnt +=1

        if 4 - x == y: #왼쪽 아래에서 오른쪽 위 대각선 해당되는 칸 확인
            rightUp += 1
            if rightUp == 5: # 마찬가지로 5칸이 모두 차면 한줄 완성
                cnt += 1

        if wid[x] == 5: #해당 행의 갯수를 +1 해준다
            cnt += 1
        if hei[y] == 5: #해당 열의 갯수를 +1 해준다
            cnt += 1

        if cnt > 2 : #위의 작업이 끝난후에 cnt 2 초과면 3줄완성이므로 몇번째로 불린 숫자인지 출력
            print((i * 5) + j + 1)
            exit()