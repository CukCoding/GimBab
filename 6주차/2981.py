import sys
r = sys.stdin.readline
def uclid(a, b) :
    num1 = a
    num2 = b
    while True :
        c = num1 % num2
        if c == 0:
            break
        else :
            num1 = num2
            num2 = c

    return num2

N = int(r())
arr = []
for i in range(N) :
    arr.append(int(r()))

arr.sort()

gap = arr[1] - arr[0]
temp = 0

for j in range(2, N) :
    temp = uclid(gap, arr[j] - arr[j - 1])
    gap = temp

result = []

d = 1
while d * d <= gap :
    if gap % d == 0 :
        temp1 = d
        temp2 = gap // d
        if temp1 == temp2 :
            result.append(temp1)
        else :
            result.append(temp1)
            result.append(temp2)
    
    d += 1

result.sort()
for k in range(1, len(result)) :
    print(result[k], end=" ")