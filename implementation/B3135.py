import sys

input = sys.stdin.readline

A, B = map(int, input().split())

N = int(input())

zupa = [int(input()) for _ in range(N)]

# print(zupa)

results = []

results.append(abs(A-B))

for val in zupa :
    results.append(abs(val - B) + 1)

print(min(results))