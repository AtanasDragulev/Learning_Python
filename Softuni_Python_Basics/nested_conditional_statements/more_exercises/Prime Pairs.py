first_start = int(input())
second_start = int(input())
first_end = int(input())
second_end = int(input())
first_end += first_start
second_end += second_start
is_first_prime = ""
is_second_prime = ""

for first in range(first_start,first_end+1):
    for num in range(2,first):
        if first % num == 0:
            is_first_prime = False
            break
        else:
            is_first_prime = True
    for second in range(second_start, second_end+1):
        for num_two in range(2, second):
            if second % num_two == 0:
                is_second_prime = False
                break
            else:
                is_second_prime = True
        if is_first_prime and is_second_prime:
            print(f"{first}{second}")


