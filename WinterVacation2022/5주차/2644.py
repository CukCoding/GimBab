import sys
r = sys.stdin.readline

N = int(r())

num1, num2 = r().split()
num1 = int(num1) - 1
num2 = int(num2) - 1

array = [[0 for row in range(N)] for col in range(N)]

m = int(r())
for i in range(m):
    x, y = list(map(int, r().split()))
    array[x - 1][y - 1] = 1
    array[y - 1][x - 1] = 1

queue = []
visit = [0 for row in range(N)]

visit[num1] = 1
for i in range(N):
    if array[num1][i] == 1:
        queue.append([i, 1])
result = -1
while(len(queue) > 0):
    des, cnt = queue.pop(0)
    if des == num2:
        result = cnt
    visit[des] = 1
    for j in range(N):
        if array[des][j] == 1 and visit[j] == 0:
            queue.append([j, cnt + 1])

print(result, end='')