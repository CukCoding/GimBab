'''
    maxNum = 0 이라는 값으로 시작,
    처음 들어온 값이 maxNum보다 큰 값이면 하나씩 스택에 집어넣고 한번 팝해서 꺼낸다.
    maxNum ~ 입력값 까지 +(push) 해주고 -(pop) 한번 한다.

    다음 값이 스택의 제일 상위 값일 경우 -(pop) 해준다

    상위 값이 아니라 maxNum보다 큰값이 들어올 경우 처음 과정을 되풀이한다.

    하지만 배열의 최상위 값도 아닌데 maxNum보다 작은 값일 경우, 팝으로 꺼낼 수 없는 경우이기 때문에
    NO를 출력한다.

    여기서 NO를 출력하고 for문을 탈출하게 되는데, for문을 정상적으로 돌고 나온 상황과 비교하기위해서
    pos 라는 변수를 둔다. 만약 NO에 걸리게 되면 pos = 1로 바뀌고
    현재코드의 최하단 if문을 통과하지 못하여 result 배열을 출력하지 못한다.
'''

import sys

def push(num) :
    result.append("+")
    stack.insert(0,num)

def pop() :
    result.append("-")
    del stack[0]

maxNum = 0
pos = 0
result = []

list = int(sys.stdin.readline())
stack = []
arr = []
for i in range(list) :
    input = int(sys.stdin.readline())
    arr.append(input)

for j in arr :
    if maxNum < j :
        for k in range(maxNum + 1, j + 1) :
            push(k)
        pop()
        maxNum = j

    elif stack[0] == j :
        pop()

    else :
        print("NO")
        pos = 1
        break

if(pos == 0) :
    for i in result :
        print(i)