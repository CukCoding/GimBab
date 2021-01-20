'''
    이분탐색은 반씩 잘라서 탐색하기에 찾고자 하는 수를 전부다 탐색하지 않고 찾을 수 있다.

    처음에 min값은 찾지 않고 max값만 찾는 이유는, 절단기의 높이가 배열에 없는 값이 될 수 있기 때문이다.
    예를들어, 입력이
    3 4
    1 2 2 가 들어가면 답은 0이 나와야 하는데 min값을 찾아서 min~max값 안에서 탐색을 해버리면
    0이 나오지 못한다.

    mid값으로 잘랐을때 가지고 싶은 나무 길이보다 합이 크면 덜 잘라야 하므로 절단기의 높이를
    mid+1~right 값에서 다시 중간값을 찾는다
    반대의 경우 left~mid-1 값에서 다시 중간값을 찾는다.

    반복문을 계속 돌다보면 left값과 right값이 같아지게 되는데 그때의 mid 값도 마찬가지로 같다
    (즉, left = right = mid)
    그럴경우에 mid값으로 나무를 다 자르고 합이 원하고자 하는 길이보다 작을경우 절단기의 높이를 한단 낮추어야하므로
    mid - 1값을 result에 저장하고 반환한다.
    반면에, 합이 원하고자 하는 길이보다 클경우, 그 값이 절단기의 최댓값이 되므로
    mid 값을 result에 저장하고 반환한다.
'''
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