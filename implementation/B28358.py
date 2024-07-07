import sys

input = sys.stdin.readline

def is_valid_date(month, day, forbidden_nums) :
    month_str = f"{month}"
    day_str = f"{day}"
    # 여기서 고민해야 하는 부분은 한 가지임. 
    # 06월 06일은 0을 포함하지만 여기서 원하는 부분은 이런 건 고민하지 않는 거임.
    # 10월이나 10일, 20, 30일 같이 뒤에 0이 붙는 거는 OK 
    # 위의 경우는 XXXX
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

#test