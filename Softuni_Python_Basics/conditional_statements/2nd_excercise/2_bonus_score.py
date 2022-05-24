number = int(input())
bonus_point = 0

if number <= 100:
    bonus_point = 5
elif number <= 1000:
    bonus_point = number * 0.2
else:
    bonus_point = number * 0.1

if number % 2 == 0:
    bonus_point += 1

if number % 10 == 5:
    bonus_point += 2

print(bonus_point)
print(number + bonus_point)