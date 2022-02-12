import sys
r = sys.stdin.readline

input = int(r())

dp = [0 for row in range(input + 1)]

if input == 0:
    print(0)
elif input == 1:
    print(1)
else:
    dp[0] = 0
    dp[1] = 1
    for i in range(2, input + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[input])