first_number = int(input())
second_number = int(input())
third_number = int(input())

for first in range(1,first_number + 1):
    if first % 2 != 0:
        continue
    for second in range(1,second_number+1):
        if second == 2 or second == 3 or second == 5 or second == 7:
            for third in range(1,third_number + 1):
                if third % 2 == 0:
                    print(first, second, third)
