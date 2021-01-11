num = int(input())
arr = []

for i in range(0, num):
    temp1 = int(input())
    arr.insert(i, temp1)

for i in range(0, num-1):
    for j in range(0, num-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

for i in arr:
    print(i)