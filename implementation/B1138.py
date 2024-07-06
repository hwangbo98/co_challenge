import sys

input = sys.stdin.readline

N = int(input())

left_person_cnt = list(map(int, input().split()))

result = [0 for _ in range(N)]

for i in range(N) :
    num = left_person_cnt[i]
    cnt = 0

    for k in range(N) :
        if cnt == num and result[k] == 0 :
            result[k] = i + 1
            break
        elif result[k] == 0 :
            cnt+=1

print(*result)
