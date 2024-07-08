import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())


goal = list(map(int, input().split()))

for i in range(N-1, 0, -1) :
    if goal[i] < goal[i-1] :
        for k in range(N-1, 0, -1) :
            if goal[i-1] > goal[k] :
                goal[i-1], goal[k] = goal[k], goal[i-1]
                goal = goal[:i] + sorted(goal[i:], reverse=True)
                print(*goal)
                exit()
print(-1)
