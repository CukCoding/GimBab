import sys
r = sys.stdin.readline

N, K = list(map(int, r().split()))

input = []
dp = [[0 for row in range(K + 1)] for col in range(N + 1)]

for i in range(N):
    W, V = list(map(int, r().split()))
    input.append([W, V])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= input[i-1][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - input[i-1][0]] + input[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])
