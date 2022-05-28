numbers = int(input())

even_num = 0
odd_num = 0

for i in range(1,numbers + 1):
    current = int(input())
    if i % 2 == 0:
        even_num += current
    else:
        odd_num += current

if even_num == odd_num:
    print(f"Yes\nSum = {even_num}")
else:
    difference = abs(even_num - odd_num)
    print(f"No\nDiff = {difference}")
