number = int(input())
is_magic = False
for num in range(1111, 10000):
    for index, digit in enumerate(str(num)):
        if digit == "0":
            is_magic = False
            break
        if number % int(digit) == 0:
            is_magic = True
        else:
            is_magic = False
            break
    if is_magic:
        print(num, end=" ")
