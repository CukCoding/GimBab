import sys
r = sys.stdin.readline

N = int(r())

dp = [0 for row in range(N + 1)]

# 1, 2, 

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[N] % 10007)