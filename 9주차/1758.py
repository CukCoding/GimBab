import sys
r = sys.stdin.readline

N = int(r())
arr = []
sum = 0

for i in range(N) :
    arr.append(int(r()))

arr.sort() #정렬하고
arr.reverse() #내림차순으로 만듬

for i in range(N) :
    temp = arr[i] - i
    if temp < 0 :
        break
    else :
        sum += temp

print(sum)