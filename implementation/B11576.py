import sys
import math

input = sys.stdin.readline

A, B = map(int, input().split())

N = int(input())

numbers = list(map(int, input().split()))

numbers.reverse()


sum_value = 0 
for i in range(N-1, -1, -1) :
    sum_value += numbers[i] * pow(A,i)

def remainder(sum_value, B) :
    share = 0
    remainder = 0
    result = []
    while(sum_value != 0 ) :
        remainder = sum_value % B
        sum_value = sum_value // B

        result.append(remainder)
    return result

value = remainder(sum_value, B)

value.reverse()

for i in value :
    print(i, end= ' ')