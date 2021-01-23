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

def solve() :
    for i in range(1, prob[0][0]+1) :
        if inputNumber(0, prob[0][i]) == False :
            continue


blank = []
prob = []
blankCnt = 0
sudoku = [list(map(int, stdin.readline().split())) for _ in range(9)]

for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            blankCnt += 1
            blank.append([i, j])


for i in blank :
    checkNum(i[0], i[1])


solve()

for i in sudoku :
    for j in i :
        print(j, end=" ")
    print("")