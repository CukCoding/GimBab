from sys import stdin

cnt = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(cnt)]


arr.sort(key = lambda x : (x[1], x[0]))
meeting = 0
data = 0
for i in range(0, cnt):
    if data <= arr[i][0]:
        meeting += 1
        data = arr[i][1]

print(meeting)