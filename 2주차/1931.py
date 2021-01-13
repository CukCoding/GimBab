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
    3번 코드 : 틀렸습니다.
    원리 : 시작시간을 먼저 오름차순 정렬, 그 후에 끝나는 시간을 오름차순 정렬하고, 끝나는 시간을 기준으로 빨리 끝나는 회의만
        고르면 하나의 회의실을 최대한 많이 사용할 수 있다.
        
    for문을 두번 돌려서 0번째 열과 1번째 열(각각 시작시간, 끝나는시간)을 퀵 솔트로 정렬하고,
    회의 시작시간이 endTime보다 클 경우, 카운트를 하면서 endTime에 선택된 회의의 끝시간을 새로 집어넣는다.
    그렇게 for문을 테스트 케이스 만큼 다 돌리면 최대한의 회의실 이용 횟수가 나온다(= metting)
'''
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

    if i > pivot and j < pivot :
        quickSort(start, i - 1, index)
        return

    swap(i, pivot)
    quickSort(start, i - 1, index)
    quickSort(i + 1, end, index)


cnt = int(input())
arr = [list(map(int, input().split())) for _ in range(cnt)]
endTime = 0
meeting = 0

for index in range(0, 2) :
    quickSort(0, cnt-1, index)

for i in range(0, cnt) :
    if arr[i][0] >= endTime :
        meeting += 1
        endTime = arr[i][1]

print(arr)
print(meeting)

