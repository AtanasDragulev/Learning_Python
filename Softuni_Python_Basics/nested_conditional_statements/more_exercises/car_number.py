first_number = int(input())
second_number = int(input())


for first in range(first_number, second_number+1):
    is_even = False
    if first % 2 == 0:
        is_even = True
    for second in range(first_number, second_number+1):
        for third in range(first_number, second_number +1):
            if (second + third) % 2 == 0:
                for forth in range(first_number, second_number+1):
                    if forth < first:
                        if is_even and forth % 2 == 0:
                            continue
                        if not is_even and forth % 2 != 0:
                            continue
                        print(f"{first}{second}{third}{forth}", end=" ")
