first_number = int(input())
second_number = int(input())

for first in range(1,first_number+1):
    for second in range(1,first_number+1):
        for third in range(97, second_number + 97):
            for forth in range(97, second_number + 97):
                for fifth in range(1,first_number + 1):
                    if fifth <= first or fifth <= second:
                        continue
                    print(f"{first}{second}{chr(third)}{chr(forth)}{fifth}",end=" ")
