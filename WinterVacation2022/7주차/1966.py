import sys
r = sys.stdin.readline

def find(n):
    chk = 0
    for i in range(n+1, 10):
        if array[i] > 0:
            chk = 1
            break
    if chk == 1:
        return True
    else:
        return False

T = int(r())
for i in range(T):
    N, M = list(map(int, r().split()))
    strong = list(map(int, r().split()))
    queue = []
    array = [0 for row in range(10)]
    for idx, i in enumerate(strong):
        mark = 0
        array[i] += 1
        if idx == M:
            mark = 1
        queue.append([i, mark])
    result = 0
    while True:
        num, m = queue.pop(0)
        cnt = find(num)
        if cnt:
            queue.append([num, m])
        elif not cnt and m == 1:
            result += 1
            break
        elif not cnt and m == 0:
            result += 1
            array[num] -= 1
    print(result)