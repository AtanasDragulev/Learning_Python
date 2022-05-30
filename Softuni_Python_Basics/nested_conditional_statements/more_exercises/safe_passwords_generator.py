first_symbol = int(input())
second_symbol = int(input())
maximum_passwords = int(input())
password_counter = 0
first = 35
second = 64

for third in range(1, first_symbol + 1):
    for forth in range(1, second_symbol + 1):
        print(f"{chr(first)}{chr(second)}{third}{forth}{chr(second)}{chr(first)}", end="|")
        password_counter += 1
        first += 1
        second += 1
        if first == 56:
            first = 35
        if second == 97:
            second = 64
        if password_counter == maximum_passwords:
            exit()
