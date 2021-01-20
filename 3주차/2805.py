import sys

def cutTree(min, max) :
    left = min
    right = max
    result = 0

    while True:
        sum = 0
        mid = (left + right) // 2
        for i in hei :
            if i > mid :
                sum = sum + (i - mid)

        if left == right :
            if sum < len :
                result = mid - 1
                break

            else :
                result = mid
                break
        else :
            if sum == len:
                result = mid
                break
            elif sum > len:
                left = mid + 1
            else:
                right = mid - 1

    return result


tree, len = sys.stdin.readline().split()
hei = list(map(int, sys.stdin.readline().split()))

tree = int(tree)
len = int(len)
max = 0

for i in hei :
    if i > max :
        max = i


result = cutTree(0, max)

print(result)