divisor = int(input())
bound = int(input())

for number in range(bound, 0, -1):
    if not number % divisor:
        print(number)
        break

