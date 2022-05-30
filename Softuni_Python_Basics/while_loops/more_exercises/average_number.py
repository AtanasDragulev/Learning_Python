numbers = int(input())
total = 0
for num in range(numbers):
    current = int(input())
    total += current
average = total / numbers
print(f"{average:.2f}")
