import sys

input = sys.stdin.readline


w, h = map(int, input().split())

N = int(input())

width = [0, w]
height = [0, h]
for _ in range(N) :
    check, ln = map(int, input().split())
    if check == 0 :
        height.append(ln)
    else :
        width.append(ln)

width.sort()
height.sort()

subtracted_width = [width[i+1] - width[i] for i in range(len(width) - 1)]
subtracted_height = [height[i+1] - height[i] for i in range(len(height) - 1)]
# print(subtracted_width, subtracted_height)

print(max(subtracted_height) * max(subtracted_width))