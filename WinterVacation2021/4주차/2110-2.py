from sys import stdin

def swap(a, b) :
    temp = loc[a]
    loc[a] = loc[b]
    loc[b] = temp

def setPivot(left, mid, right) :
    if loc[left] > loc[mid] :
        swap(left, mid)
    if loc[mid] > loc[right] :
        swap(mid, right)
    if loc[mid] < loc[left] :
        swap(mid, left)

def sort(left, right) :
    mid = left + ((right - left) // 2)

    setPivot(left, mid, right)

    if right - left < 3 :
        return

    i = left + 1
    j = right - 1
    pivot = right - 1

    swap(mid, pivot)

    while i < j :
        while i < right and loc[i] <= loc[pivot] :
            i += 1
        while j > left and loc[j] >= loc[pivot] :
            j -= 1

        if i < j :
            swap(i, j)
    if i > pivot :
        swap(mid, pivot)
        sort(left, i - 1)
        return

    swap(i, pivot)
    sort(left, i - 1)
    sort(i + 1, right)

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

sort(0, house - 1)

if wifi == 2 :
    print(loc[house - 1] - loc[0])
else :
    print(search(loc[0], loc[house - 1]))