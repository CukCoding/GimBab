'''
    두번째 코드 원리(재귀 호출 방식) - 1416ms
        1. 0(빈칸)의 좌표를 blank 배열에 저장
        2. 각 빈칸마다 들어갈 수 있는 수들을 prob 배열에 저장 그러면 blank배열과 prob배열은 같은 행을 가짐
        3. 첫번째 자리부터 들어갈 수 있는 수를 inputNumber로 넘겨서 가로, 세로, 3x3 부분에 겹치는 숫자가 있는지 확인하고
        있을 경우 False, 없을 경우 해당 자리에 그 수를 넣고 다시 inputNumber로 다음 빈칸을 채워나간다.
        4. 만약, blank 배열의 제일 끝(가장 마지막 빈칸)에 도달할 경우, 아무 문제가 없는 것이므로, 마지막 빈칸을 숫자로 채우고
        True를 반환한다.
        5. 하나라도 False가 나올 경우 함수는 종료되고, 이전 호출 함수에서 다음에 들어갈 수 있는 수가 있을경우
        (prob 배열에 숫자가 여러개 존재해서 다 확인해야하므로), 다른 수를 넣는다
        6. prob배열에서 해당 칸의 모든 경우의 수를 다 돌 경우 함수는 False를 반환해야 하며 이전 호출 함수로 되돌아가기전에
        해당 칸을 0으로 만들고 종료한다.
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

def inputNumber(location, number) :
    x = blank[location][0]
    y = blank[location][1]
    quadX = (x // 3) * 3
    quadY = (y // 3) * 3
    cnt = 0


    for j in range(9):
        if sudoku[x][j] == number:
            cnt += 1
            break
        elif sudoku[j][y] == number:
            cnt += 1
            break
        elif sudoku[quadX + (j // 3)][quadY + (j % 3)] == number:
            cnt += 1
            break

    if cnt > 0 :
        return False
    elif location + 1 == blankCnt :
        sudoku[x][y] = number
        return True
    else :
        sudoku[x][y] = number
        for i in range(1, prob[location + 1][0] + 1) :
            if inputNumber(location + 1, prob[location + 1][i]) == False :
                continue
            else :
                return True

        sudoku[x][y] = 0
        return False

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