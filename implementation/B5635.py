import sys

input = sys.stdin.readline

N = int(input())

birthday_dict = {}
for _ in range(N) :
    name, day, month, year = map(str, input().split())
    month = int(month)
    day = int(month)
    new_month = f"{month:02d}"
    new_day = f"{day:02d}"
    birthday_dict[name] = year + new_month + new_day


sorted_birthday = sorted(birthday_dict.items(), key = lambda x : x[1])

print(sorted_birthday[-1][0])
print(sorted_birthday[0][0])