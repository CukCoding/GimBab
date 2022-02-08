import sys

r = sys.stdin.readline

N, K = list(map(int, r().split()))

arr = []
for i in range(1, N + 1):
    arr.append(i)

result = []
while (len(arr) > 0):
    for i in range(K - 1):
        t = arr.pop(0)
        arr.append(t)
    num = arr.pop(0)
    result.append(num)

print("<", end='')
for i in range(len(result) - 1):
    print(result[i], end='')
    print(", ", end='')
print(result[len(result) - 1], end='')
print(">", end='')