'''
    첫번째 코드 원리(재귀 호출 방식) - 2520ms
        앞의 코드와 거의 동일하나, inputNumber에서 해당 칸에 숫자가 들어갈 수 있는지 없는지를 확인하는 방식에
        조금 차이가 있다. 원래라면 해당 칸의 가로와 세로를 전부 확인해야 했으나, 사실 for문을 의미없게 확인하는 것이 된다.
        왜냐하면 어짜피 prob배열에 들어가 있는 수는 가로 세로 3x3 에서 같은 숫자가 없기 때문에
        이미 나온 숫자들이기 때문에, 그 전 함수에서 해당 가로나 세로나 3x3 에 어떤 숫자가 들어갔는지를 기억하고
        그 숫자들로만 비교한다.

        그래서 wid배열 hei배열 sq(3x3) 배열이 따로 있고, 숫자가 들어갈때마다 0번째에는 갯수를 조정해주고, 1번째부터 들어간 숫자들을 기억한다

        예를 들면, (0,0)이 빈칸이어서 6을 넣게 되면 wid[0]배열에 6, hei[0]배열에 6, sq[0] 배열에 6이 들어간다
        그러고 나서 (0,6) 빈칸을 채우기 위해서는 해당 가로와 세로를 전부 비교하는게 아니라 그 이전에 해당 가로나 세로나 3x3에 들어가서 변동된 값들이
        있는지만 비교해주면 된다 그러므로 wid[0]배열, hei[6]배열, sq[0]배열에 들어가 있는 숫자들과 같은게 있는지만 확인해준다.

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

def widCheck(x, number) :
    for i in range(1, wid[x][0] + 1):
        if wid[x][i] == number:
            return False
    return True

def heiCheck(y, number) :
    for i in range(1, hei[y][0] + 1):
        if hei[y][i] == number:
            return False
    return True

def sqCheck(temp, number) :
    for i in range(1, sq[temp][0] + 1):
        if sq[temp][i] == number:
            return False
    return True

def inputNumber(location, number) :
    x = blank[location][0]
    y = blank[location][1]
    quadX = (x // 3) * 3
    quadY = (y // 3) * 3
    temp = ((quadX + 1) + (quadY // 3)) - 1

    cnt = 0

    if widCheck(x, number) == False or heiCheck(y, number) == False or sqCheck(temp, number) == False :
        cnt += 1

    if cnt > 0 :
        return False
    elif location + 1 == blankCnt :
        sudoku[x][y] = number
        return True
    else :
        sudoku[x][y] = number
        wid[x][wid[x][0] + 1] = number
        hei[y][hei[y][0] + 1] = number
        sq[temp][sq[temp][0] + 1] = number
        wid[x][0] += 1
        hei[y][0] += 1
        sq[temp][0] += 1
        for i in range(1, prob[location + 1][0] + 1) :
            if inputNumber(location + 1, prob[location + 1][i]) == False :
                continue
            else :
                return True
        sudoku[x][y] = 0
        wid[x][0] -= 1
        hei[y][0] -= 1
        sq[temp][0] -= 1
        return False


wid = [[0 for _ in range(10)] for _ in range(10)]
hei = [[0 for _ in range(10)] for _ in range(10)]
sq = [[0 for _ in range(10)] for _ in range(10)]

blank = []
prob = []
blankCnt = 0
sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]

for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            blankCnt += 1
            blank.append([i, j])
            checkNum(i, j)

'''
for i in blank :
    checkNum(i[0], i[1])
'''

for i in range(1, prob[0][0]+1) :
    if inputNumber(0, prob[0][i]) == False :
        continue

for i in sudoku :
    for j in i :
        print(j, end=" ")
    print("")