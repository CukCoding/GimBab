'''
    정렬을 sort()를 이용해서 하고
    배열의 최댓값과 최솟값의 차이를 이분탐색하여, 최댓값에 도달하게 한다
'''
from sys import stdin
def search(left, right) :
    result = 0
    maxGap = right - left
    minGap = 1
    while True :
        mid = minGap + ((maxGap - minGap) // 2)
        before = left
        cnt = 1

        for i in loc[1:]:
            sub = i - before
            if sub >= mid:
                cnt += 1
                before = i

        if minGap == maxGap :
            if cnt < wifi :
                result = mid - 1
                break
            else :
                result = mid + 1
                break
        else :
            if cnt > wifi:
                minGap = mid + 1
            elif cnt < wifi:
                maxGap = mid
            else:
                minGap = mid + 1

    return result

house, wifi = stdin.readline().split()

house = int(house)
wifi = int(wifi)

loc = []

for i in range(house) :
    loc.append(int(stdin.readline()))

loc.sort()

if wifi == 2 :
    print(loc[house - 1] - loc[0])
else :
    print(search(loc[0], loc[house - 1]))