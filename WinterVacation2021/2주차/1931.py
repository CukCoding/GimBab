'''
1번 코드 : 시간초과
def fun(endTime) :
    latest = 0
    maxNum = 0
    for i in range(cnt) :
        if arr[i][0] >= endTime :

            latest += 1

            if arr[i][2] != -1:
                temp1 = arr[i][2]

                if maxNum < temp1 :
                    maxNum = temp1
            else :
                temp2 = fun(arr[i][1])

                if maxNum < temp2 :
                    maxNum = temp2

                if arr[i][2] < temp2:
                    arr[i][2] = temp2

    if latest == 0 :
        return 0

    return maxNum + 1

cnt = int(input())

result = 0

arr = [list(map(int, input().split())) for _ in range(cnt)]
for i in range(cnt) :
    arr[i].append(-1)

for i in range(cnt) :
    if arr[i][2] != -1 :
        tmp = arr[i][2]
        if result < tmp:
            result = tmp
    else :
        tmp = fun(arr[i][0])
        if result < tmp:
            result = tmp

print(result)
'''


'''
2번코드 : 시간초과
endTime = 0
number = 0
meeting = 0


cnt = int(input())
arr = [list(map(int, input().split())) for _ in range(cnt)]

while True :
    loopCnt = 0
    nextConf = 0
    for i in range(0, cnt):
        if arr[i][0] > endTime and arr[i][1] == number:
            nextConf += 1
            endTime = number
            meeting += 1
            break

        elif arr[i][0] > endTime :
            loopCnt += 1
    if loopCnt == 0 and nextConf == 0:
        break
    else :
        number += 1

print(meeting)
'''

'''
    3번 코드 : 맞았습니다.
    원리 : 시작시간을 먼저 오름차순 정렬, 그 후에 끝나는 시간을 오름차순 정렬하고, 끝나는 시간을 기준으로 빨리 끝나는 회의만
        고르면 하나의 회의실을 최대한 많이 사용할 수 있다.
        
    for문을 두번 돌려서 0번째 열과 1번째 열(각각 시작시간, 끝나는시간)을 퀵 솔트로 정렬하고,
    회의 시작시간이 endTime보다 클 경우, 카운트를 하면서 endTime에 선택된 회의의 끝시간을 새로 집어넣는다.
    그렇게 for문을 테스트 케이스 만큼 다 돌리면 최대한의 회의실 이용 횟수가 나온다(= metting)
    
    퀵 정렬의 규칙 : 피봇을 임의로 정해서 피봇을 기준으로 왼쪽에는 피봇보다 작은값, 오른쪽에는 피봇보다 큰 값으로 정렬한다.
                    더이상 바꿀게 없을 경우 왼쪽배열과 오른쪽 배열을 다시 퀵 정렬로 돌린다.
    1. 피봇을 배열의 첫번째 값으로 잡을 경우, 완전히 정렬되어 있는 배열에서 시간복잡도의 상승으로 최악이다. 그래서 중간값 퀵정렬을 사용한다.
    
    2. 중간값 퀵정렬은 배열의 가장 첫번째 값, 중간값, 마지막 값을 먼저 비교해서 정렬한다 -> setPivot 함수
       그러면 첫번째 값 < 중간값 < 마지막값 순서로 정렬이 된다.
    
    3. 중간값을 피봇으로 삼고, 제일 끝에서 한칸 전으로 옮긴다.(마지막 칸이 아닌 이유는 2번 과정에서 이미 마지막칸은 피봇보다 큰 값이
       들어가 있으므로 정렬에 넣을 필요가 없다.
    
    4. i도 마찬가지로 맨 앞에 칸은 이미 피봇보다 작으므로 0번째가 아닌 +1 번째 부터 비교하면서 올라가고 j는 피봇부터 비교하면서 내려온다.
    
    5. i가 j보다 작은 상태이면 i와 j를 swap, i가 j보다 크면 while 문을 탈출한다. 그러고 만약 i가 피봇보다 큰쪽에 있게 된다면,
       피봇 앞에 다 작은 값이 놓여져있는것이므로 3번 과정에서 바꾸었던 것을 원위치 시키고 함수를 종료시킨다
       
    6. 만약 i가 j보다 크지만 피봇보다는 앞에 있는 위치라면, i와 피봇을 바꾸고 while문을 탈출한다. 그다음 i를 기준으로 왼쪽배열,
       오른쪽 배열로 나눈 뒤에 각각 다시 퀵정렬 함수로 정렬한다. 이때 범위는 start < i - 1 과 i + 1 < end 가 된다.
       
    7. 소트 함수 앞부분에는 end - start < 3 이하일때 함수를 종료하는 문 이 있는데, 이것은 배열의 크기가 3이하면, setPivot 함수에서
       맨 앞, 중간, 끝을 정렬해버리는 순간 더이상 피봇을 이용한 정렬이 필요가 없기 때문에, 종료시킨다.
'''
from sys import stdin
def setPivot(start, mid, end, index) :
    if arr[mid][index] < arr[start][index] :
        swap(mid, start)
    if arr[mid][index] > arr[end][index] :
        swap(mid, end)
    if arr[mid][index] < arr[start][index] :
        swap(mid, start)


def swap(a, b) :
    temp1 = arr[b][0]
    temp2 = arr[b][1]

    arr[b][0] = arr[a][0]
    arr[b][1] = arr[a][1]

    arr[a][0] = temp1
    arr[a][1] = temp2

def quickSort(start, end, index) :
    mid = ((end - start) // 2) + start

    setPivot(start, mid, end, index)

    if end - start < 3 :
        return

    swap(mid, end - 1)
    pivot = end - 1
    i = start + 1
    j = end - 1

    while i < j :
        while i < end and arr[i][index] <= arr[pivot][index] :
            i += 1

        while j > start and arr[j][index] >= arr[pivot][index] :
            j -= 1

        if i < j :
            swap(i, j)

    if i > pivot:
        swap(mid, pivot)
        quickSort(start, i - 1, index)
        return

    swap(i, pivot)
    quickSort(start, i - 1, index)
    quickSort(i + 1, end, index)


cnt = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(cnt)]
endTime = 0
meeting = 0

for index in range(0, 2) :
    quickSort(0, cnt-1, index)

for i in range(0, cnt) :
    if arr[i][0] >= endTime :
        meeting += 1
        endTime = arr[i][1]

print(meeting)

