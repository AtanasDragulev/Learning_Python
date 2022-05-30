hundreds_limit = int(input())
tens_limit = int(input())
singles_limit = int(input())

for hundreds in range(2, hundreds_limit+1, 2):
    for tens in range(2,tens_limit+1):
        is_not_prime = False
        if 7 > tens < 2:
            continue
        for num in range(2,tens):
            if tens % num == 0:
                is_not_prime = True
        if is_not_prime:
            continue
        for singles in range(2, singles_limit+1,2):
            print(hundreds, tens, singles)