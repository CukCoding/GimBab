import sys

r = sys.stdin.readline

T = int(r().strip())
for i in range(T):
    H, W, N = list(map(int, r().split()))
    # 층수, 호실
    if N % H == 0:
        step = H * 100
        room = N // H
    else:
        step = (N % H) * 100
        room = (N // H) + 1

    print(step + room)