#약수 구하는 과정에서 아무래도 시간초과 뜨는듯...
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

for j in range(2, gap + 1) :
    if gap % j == 0:
        result.append(j)

for k in result :
    print(k, end=" ")