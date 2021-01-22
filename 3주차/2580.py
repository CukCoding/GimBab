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

def inputNumber(cnt, number) :
    print("함수진입")

    x = blank[cnt][0]
    y = blank[cnt][1]
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
    elif cnt + 1 > blankCnt :
        return True
    else :
        sudoku[x][y] = number
        for i in range(1, prob[cnt + 1][0] + 1) :
            if inputNumber(cnt + 1, prob[cnt + 1][i]) == False :
                continue
            else :
                break

def solve(blankCnt) :
    for i in range(blankCnt) :
        if prob[i][0] == 1 :
            sudoku[blank[i][0]][blank[i][1]] = prob[i][1]
        else :
            for j in range(1, prob[i][0] + 1) :
                if inputNumber(i, prob[i][j]) == False :
                    continue
                else :
                    break
            if sudoku[blank[blankCnt-1][0]][blank[blankCnt-1][1]] != 0 :
                break



blank = []
prob = []
blankCnt = 0
sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]

for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            blankCnt += 1
            blank.append([i, j])

print("빈칸갯수", blankCnt)

for i in blank :
    checkNum(i[0], i[1])

print(prob)

solve(blankCnt)

for i in sudoku :
    for j in i :
        print(j, end=" ")
    print("")