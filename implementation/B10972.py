import sys

input = sys.stdin.readline

N = int(input())

line = list(map(int, input().split()))

print(line)

def predict_next_num(line, N) :
    
    for i in range(N-1, 0, -1) :
        if line[i] > line[i-1] :
            for k in range(i-1, 0, -1) :
                if line[i] > line[k] :
                    line[i], line[k] = line[k], line[i]
                    str_ = line[:i] + sorted(line[i:] )
                    print(str_)
                    exit()

predict_next_num(line,N)