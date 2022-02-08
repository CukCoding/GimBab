import sys
r = sys.stdin.readline

N = int(r())
com = [[0 for col in range(N)] for row in range(N)]

K = int(r())
for i in range(K):
    input = r().split()
    com[int(input[0]) - 1][int(input[1]) - 1] = 1
    com[int(input[1]) - 1][int(input[0]) - 1] = 1

queue = []
for i in range(N):
    if com[0][i] == 1:
        queue.append(i)

cnt = 0;
visit = [0 for col in range(N)]
visit[0] = 1
while len(queue) > 0 :
    num = queue.pop(0)
    if visit[num] == 0:
        visit[num] = 1
        cnt += 1
        for j in range(N):
            if com[num][j] == 1:
                queue.append(j)

print(cnt, end='')