numbers = int(input())

left_num = 0
right_num = 0

for i in range(numbers):
    current = int(input())
    left_num += current

for i in range(numbers):
    current = int(input())
    right_num += current

if left_num == right_num:
    print(f"Yes, sum = {left_num}")
else:
    difference = abs(left_num - right_num)
    print(f"No, diff = {difference}")
