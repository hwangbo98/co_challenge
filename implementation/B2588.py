import sys

input = sys.stdin.readline

A = int(input())
B = int(input())

results = []
for i in str(B):
    results.append(int(i) * A)


results.reverse()
total = 0
for k, val in enumerate(results) :
    total += pow(10,k) * val

results.append(total)

for i in results :
    print(i)