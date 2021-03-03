import sys
r = sys.stdin.readline

N = int(r())
arr = list(map(int, r().split()))
cnt = 0

for i in range(N) :
    if arr[i] == 1 :
        continue
    pos = 0
    num = arr[i]
    j = 1
    while j * j <= num :
        if num % j == 0 :
            if j > 1 :
                pos = 1
                break
        j += 1
    if pos == 0 :
        cnt += 1

print(cnt)