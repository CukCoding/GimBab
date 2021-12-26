'''
    결과를 각각 테스트 케이스가 끝날때마다 출력하면 ValueError가 떠버린다.
    그래서 result 배열에 모든 결과를 저장해놓고 있다가 입력이 전부 끝나면
    순차적으로 출력해줘야한다.
'''
from sys import stdin
from collections import deque

test = int(stdin.readline())
q = deque()
result = []

for i in range(test) :
    checkReverse = 0 # 거꾸로 뒤집었는지 안뒤집었는지 체크하는 변수
    errorCheck = False # error가 뜨면 반복문을 빠져나가기 위한 변수

    cmd = stdin.readline().strip()
    count = int(stdin.readline())
    arr = stdin.readline().strip()[1:-1]

    if not arr == '' : # arr가 공백 배열이 아닐 경우 콤마를 기준으로 arr에 있는걸 deque에 순서대로 쌓는다
        q = deque(arr.split(","))

    for j in cmd :
        if j == 'R' :
            checkReverse = (checkReverse + 1) % 2 # Reverse는 0 또는 1의 값으로 판단할 수 있다
        else :
            if len(q) == 0 : # D가 나왔는데 배열이 비어있는경우
                result.append('error')
                errorCheck = True
                break
            elif checkReverse == 1: # D인데 거꾸로 뒤집어져있는경우
                q.pop()
            else : # D인데 정상 방향 수열인 경우
                q.popleft()

    if errorCheck == True : # error가 발생하면 다음 명령어로 넘어간다
        continue
    elif checkReverse == 1: # 방향이 거꾸로인 경우 temp배열에 뒤에서부터 앞으로 순차적으로 넣는다
        temp = []
        temp.append('[')
        for k in range(len(q) - 1, -1, -1) :
            if k == 0 : # 마지막 숫자 뒤에는 콤마를 넣으면 안된다
                temp.append(q[k])
            else :
                temp.append(q[k])
                temp.append(',')
        temp.append(']')
        result.append(temp)
    else : # 정상 방향인 경우 0번째 부터 순서대로 넣는다
        temp = []
        temp.append('[')
        for k in range(len(q)) :
            if k == len(q) - 1 : # 제일 마지막 숫자 뒤에는 콤마를 넣으면 안된다.
                temp.append(q[k])
            else :
                temp.append(q[k])
                temp.append(',')
        temp.append(']')
        result.append(temp)

    q.clear() #q의 작업이 끝낫으므로 q의 원소를 비워준다.

for i in result : #결과를 출력한다
    for j in i[0:] :
        print(j, end="")
    print("")