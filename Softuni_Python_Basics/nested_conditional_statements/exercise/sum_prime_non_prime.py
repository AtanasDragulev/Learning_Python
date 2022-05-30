sum_prime = 0
sum_non_prime = 0
is_prime = ""
while True:
    current = input()
    if current == "stop":
        break
    number = int(current)
    if number < 0:
        print("Number is negative.")
        continue
    for num in range(2, number):
        if (number % num) == 0:
            is_prime = False
            break
    else:
        is_prime = True

    if is_prime:
        sum_prime += number
    else:
        sum_non_prime += number

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
