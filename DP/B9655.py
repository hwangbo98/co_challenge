import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

dp[0] = 0
dp[1] = 1
dp[2] = 0

for i in range(4, N+1) :
    if dp[i-1] == 1 or dp[i-3] == 1 :
        dp[i] = 0
    else :
        dp[i] = 1

print("SK" if dp[N] == 1 else "CY")