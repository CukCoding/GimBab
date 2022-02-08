num = int(input())
arr = []

for i in range(0, num):
    temp1 = int(input())
    arr.insert(i, temp1)

for i in range(1, num):
    temp2 = arr[i]
    for j in range(1, i+1):
        if(temp2 < arr[i - j]):
            arr[i-j+1] = arr[i-j]
            arr[i-j] = temp2
        elif(temp2 > arr[i-j]):
            break

for i in arr:
    print(i)