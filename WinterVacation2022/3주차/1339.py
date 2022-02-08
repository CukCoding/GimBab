import sys
r = sys.stdin.readline

N = int(r())
alpha = [[0 for col in range(2)] for row in range(26)]
for i in range(26):
    alpha[i][0] = ord('A') + i
for i in range(0, N):
    input = r().rstrip()
    for idx, j in enumerate(input):
        loc = len(input) - idx - 1
        alpha[ord(j)-ord('A')][1] += (10 ** loc)

alpha.sort(key=lambda x:x[1], reverse=True)

num = 9
sum = 0
for i in range(10):
    sum += (alpha[i][1] * num)
    num -= 1

print(sum, end='')