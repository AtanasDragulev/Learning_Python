numbers = int(input())
odd_sum = 0.00
even_sum = 0.00
odd_min = 1000000000.0
odd_max = -1000000000.0
even_min = 1000000000.0
even_max = -1000000000.0

for num in range(1, numbers + 1):
    current = float(input())
    if num % 2 != 0:
        odd_sum += current
        if odd_max < current:
            odd_max = current
        if odd_min > current:
            odd_min = current
    else:
        even_sum += current
        if even_max < current:
            even_max = current
        if even_min > current:
            even_min = current

print(f"OddSum={odd_sum:.2f},")
if odd_min != 1000000000.0:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print("OddMin=No,")
    print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
if even_min != 1000000000.0:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print("EvenMin=No,")
    print("EvenMax=No")
