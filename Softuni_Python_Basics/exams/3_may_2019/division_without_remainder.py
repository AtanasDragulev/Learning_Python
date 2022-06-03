numbers = int(input())
two_counter = 0
three_counter = 0
four_counter = 0
for i in range(numbers):
    current = int(input())
    if current % 2 == 0:
        two_counter += 1
    if current % 3 == 0:
        three_counter += 1
    if current % 4 == 0:
        four_counter += 1

two_counter = (two_counter / numbers) * 100
three_counter = (three_counter / numbers) * 100
four_counter = (four_counter / numbers) * 100
print(f"{two_counter:.2f}%")
print(f"{three_counter:.2f}%")
print(f"{four_counter:.2f}%")
