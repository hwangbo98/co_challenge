import sys

input = sys.stdin.readline

N = int(input())

result = []
for i in range(N):
    class_X = list(map(int, input().split()))
    result.append(class_X[1:])

for k, X in enumerate(result):
    X.sort(reverse=True)
    max_score = X[0]
    min_score = X[-1]
    largest_gap = max(X[j] - X[j + 1] for j in range(len(X) - 1))
    
    print(f'Class {k + 1}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {largest_gap}')