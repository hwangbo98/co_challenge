import sys

input = sys.stdin.readline

def is_valid_date(month, day, forbidden_nums) :
    month_str = f"{month}"
    day_str = f"{day}"

    for k in month_str + day_str :
        if int(k) in forbidden_nums :
            return False
    
    return True

def count_valid_nums(result) :

    forbidden_month = [i for i, val in enumerate(result) if val == 1]
    
    count = 0
    days_month = [31,29,31,30,31,30,31,31,30,31,30,31]

    for month in range(1, 13) :
        for day in range(1, days_month[month-1] +1) :
            if is_valid_date(month, day, forbidden_month) :
                count+=1

    return count

T = int(input())
outputs = []
for _ in range(T) :
    result = list(map(int, input().split()))
    outputs.append(count_valid_nums(result))


for k in outputs :
    print(k)

