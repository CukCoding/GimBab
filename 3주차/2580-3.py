'''
    3번째 코드 : python 3 로 합격!!
    원리 :
        일단 1, 2번 코드에서 하듯이 해당 빈칸에 어떤 숫자가 들어갈 수 있는지 배열에 저장한다.

        빈칸 좌표 = blank배열
        들어갈 수 있는 숫자 = prob배열
        첫번째 빈칸 blank[0]에 들어갈 수 있는 숫자는 prob[0]에 저장되있는 숫자....
        ...
        N번재 빈칸 blank[N]에 들어갈 수 있는 숫자는 prob[N]

        inputNumber 함수에서 0번째 부터 시작한다
        blank[0]에 있는 x, y 값 좌표를 가져오고, 9개의 3x3 사각형 중에 몇번째인지도 알아낸다(=quad)

        그러고나서 number에 prob에 있는 값을 차례차례 불러오는데 불러와서 다음 단계로 넘어가기 전에
        이미 들어가있는 숫자인지를 검사한다.

        검사하는 방식은 다음과 같다. 예를들어 (0, 6)에 9라는 숫자를 이전 단계에서 집어넣었다면
        가로배열(wid), 세로배열(hei), 3x3배열(sq)에 저장을 하는데
        wid[0][9] = 1  // wid[x좌표][숫자값]
        hei[6][9] = 1 // hei[y좌표][숫자값]
        sq[2][9] = 1 // sq[몇번째 네모][숫자값]
        이렇게 저장을 해놓는다. 그러면 다음에 확인을 할때 굳이 for문을 쓰지 않고 해당 x좌표에 이 숫자값이 있다면
        1로 표시되기 때문에 바로 구분을 할 수 있다.

        그러고 blankCnt에서 총 빈칸갯수를 세고, inputNumber함수가 blankCnt만큼 호출되게 되면
        if문에서 조건을 확인하고 스도쿠를 출력한뒤 함수를 exit()로 종료한다.
'''
from sys import stdin

def checkNum(x, y) :
    temp = [0]
    quadX = (x // 3) * 3
    quadY = (y // 3) * 3
    pos = 0
    for i in range(1, 10) :
        cnt = 0

        for j in range(9) :
            if sudoku[x][j] == i :
                cnt += 1
                break
            elif sudoku[j][y] == i :
                cnt += 1
                break
            elif sudoku[quadX + (j // 3)][quadY + (j % 3)] == i:
                cnt += 1
                break

        if cnt == 1 :
            continue
        else :
            pos += 1
            temp[0] = pos
            temp.append(i)

    prob.append(temp)

def inputNumber(location) :
    if location == blankCnt :
        for i in sudoku:
            for j in i:
                print(j, end=" ")
            print("")
        exit()

    x = blank[location][0]
    y = blank[location][1]
    quad = ((x // 3) * 3) + (y // 3)

    for i in range(1, prob[location][0] + 1) :
        number = prob[location][i] - 1
        if wid[x][number] == 1 or hei[y][number] == 1 or sq[quad][number] == 1 :
            continue
        else :
            sudoku[x][y] = number + 1
            wid[x][number] = 1
            hei[y][number] = 1
            sq[quad][number] = 1
            inputNumber(location + 1)
            sudoku[x][y] = 0
            wid[x][number] = 0
            hei[y][number] = 0
            sq[quad][number] = 0



wid = [[0 for _ in range(9)] for _ in range(9)]
hei = [[0 for _ in range(9)] for _ in range(9)]
sq = [[0 for _ in range(9)] for _ in range(9)]

sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]

blank = []
prob = []
blankCnt = 0

for i in range(9) :
    for j in range(9) :
        k = sudoku[i][j]
        temp = ((i // 3) * 3) + (j // 3)
        if sudoku[i][j] == 0 :
            blankCnt += 1
            blank.append([i, j])
            checkNum(i, j)

inputNumber(0)
