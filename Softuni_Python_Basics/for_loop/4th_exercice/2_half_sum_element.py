numbers = int(input())
sum_numbers = 0
max_number = 0

for i in range(numbers):
    current = int(input())
    if max_number < current or i == 0:
        max_number = current
    sum_numbers += current

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    difference = abs((max_number - (sum_numbers - max_number)))
    print("No")
    print(f"Diff = {difference}")
