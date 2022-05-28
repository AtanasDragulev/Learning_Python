numbers = int(input())
current = int(input())
current_b = int(input())
sum_a = current + current_b
difference = 0
sum_b = 0

for pair in range(1, numbers):
    current = int(input())
    current_b = int(input())
    sum_b = current + current_b

    if abs(sum_b - sum_a) > difference:
        difference = abs(sum_b - sum_a)

    sum_a = sum_b

if difference == 0:
    print(f"Yes, value={sum_a}")
else:
    print(f"No, maxdiff={difference}")
