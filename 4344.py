avg = 0
result = []

testSize = int(input())

for i in range(0, testSize):
    sum = 0
    cnt = 0
    arr = list(map(int, input().split()))
    for j in range(1, arr[0] + 1):
        sum += arr[j]
    avg = sum / arr[0]

    for j in range(1, arr[0] + 1):
        if arr[j] > avg:
            cnt += 1
    result.append((cnt / arr[0]) * 100)

for i in result:
    print('%.3f' % i + "%")
