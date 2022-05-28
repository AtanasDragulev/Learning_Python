import sys

numbers = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(numbers):
    current = int(input())

    if current > max_number:
        max_number = current
    if current < min_number:
        min_number = current

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
