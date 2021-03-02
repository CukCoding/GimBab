'''
    정렬을 사용해서 풀이할려고 했지만 시간초과..
'''

import sys
r = sys.stdin.readline

def swap(a, b) :
    temp1 = P[b][0]
    temp2 = P[b][1]

    P[b][0] = P[a][0]
    P[b][1] = P[a][1]

    P[a][0] = temp1
    P[a][1] = temp2

def setPivot(first, mid, last) :
    if P[first][0] > P[mid][0] :
        swap(first, mid)
    if P[mid][0] > P[last][0] :
        swap(mid, last)
    if P[first][0] > P[mid][0] :
        swap(first, mid)

def sort(first, last) :
    mid = (first + last) // 2
    setPivot(first, mid, last)
    if last - first > 2 :
        i = first + 1
        j = last - 1
        pivot = last - 1
        swap(mid, j)

        while i < j :
            while i < last and P[i][0] <= P[pivot][0] :
                i += 1
            while j > first and P[j][0] >= P[pivot][0] :
                j -= 1

            if i < j :
                swap(i, j)
        if i > pivot :
            swap(mid, pivot)
            sort(first, i - 1)
            return
        swap(i, pivot)
        sort(first, i - 1)
        sort(i + 1, last)

N = int(r())
P = []
result = 0

for i in range(N) :
    temp = list(map(int, r().split()))
    P.append(temp)

sort(0, N - 1)

for i in range(N) :
    cnt = 0
    d = P[i][0]
    c = P[i][1]
    for j in range(i) :
        if P[j][0] == d :
           cnt += 1
        if P[j][1] > c :
            cnt += 1
    if cnt == i :
        result += 1
    else :
        continue

print(result)

