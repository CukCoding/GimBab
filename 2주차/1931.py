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
    tmp = fun(arr[i][0])
    if result < tmp :
        result = tmp

print(result)