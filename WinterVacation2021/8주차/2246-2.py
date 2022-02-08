'''
    일일히 다 비교하는것이라서 50% 이상에서 시간초과가 뜬다
'''
import sys
r = sys.stdin.readline

N = int(r())
P = []
cnt = 0

for i in range(N) :
    P.append(list(map(int, r().split())))

for i in range(N) :
    d = P[i][0]
    c = P[i][1]
    pos = 0
    for j in range(N) :
        if i != j :
            if P[j][1] < c and P[j][0] <= d:  # 가격은 싼데 거리가 현재 거리보다 가깝거나 또는 같으면 브레이크 조건
                pos = 1
                break
            if P[j][0] < d and P[j][1] <= c:  # 거리는 가까운데 가격이 지금거 보다 싸면 브레이크 조건
                pos = 1
                break
    if pos == 0 :
        cnt += 1

print(cnt)