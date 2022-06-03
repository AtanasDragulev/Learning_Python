first_number = int(input())
second_number = int(input())
third_number = int(input())
for ticket in range(first_number, second_number):
    if ticket % 2 == 0:
        continue
    for second in range(1, third_number):
        for third in range(1, int(third_number/2)):
            if (ticket + second + third) % 2 != 0:
                print(f"{chr(ticket)}-{second}{third}{ticket}")
