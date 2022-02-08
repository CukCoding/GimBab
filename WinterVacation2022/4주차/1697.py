import sys
r = sys.stdin.readline

N, K = r().split(" ")

N = int(N)
K = int(K)

visit = [0 for col in range(100001)]

queue = []
queue.append([N, 0])
result = -1
if K <= N:
    result = N - K
else:
    while(len(queue) > 0):
        cur = queue.pop(0)
        if cur[0] == K:
            result = cur[1]
            break;
        elif cur[0] >= 0 and cur[0] <= 100000:
            if visit[cur[0]] == 0:
                visit[cur[0]] = 1
                queue.append([cur[0] - 1, cur[1] + 1])
                queue.append([cur[0] + 1, cur[1] + 1])
                queue.append([cur[0] * 2, cur[1] + 1])


print(result, end='')