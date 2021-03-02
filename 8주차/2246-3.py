import sys
r = sys.stdin.readline

N = int(r())
P = []
result = 0

for i in range(N) :
    temp = list(map(int, r().split()))
    P.append(temp)

P.sort(key=lambda x : (x[0], x[1]))

for i in range(N) :
    pos = 0
    j = 0
    d = P[i][0]
    c = P[i][1]
    while j <= i :
        if i != j and P[j][1] <= c :
            pos = 1
            break
        j += 1

    if pos == 0 :
        result += 1

print(result)