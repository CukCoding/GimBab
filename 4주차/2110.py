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

def search(gap) :
    print("차이")

house, wifi = stdin.readline().split()

house = int(house)
wifi = int(wifi)

loc = []

for i in range(house) :
    loc.append(int(stdin.readline()))

sort(0, house - 1)
maxGap = loc[house-1] - loc[0]

search(maxGap)

print(loc)