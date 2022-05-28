numbers = int(input())
p_one = 0
p_two = 0
p_three = 0
p_four = 0
p_five = 0

for i in range(numbers):
    current = int(input())
    if current < 200:
        p_one += 1
    elif current < 400:
        p_two += 1
    elif current < 600:
        p_three += 1
    elif current < 800:
        p_four += 1
    else:
        p_five += 1

p_one = (p_one / numbers) * 100
p_two = (p_two / numbers) * 100
p_three = (p_three / numbers) * 100
p_four = (p_four / numbers) * 100
p_five = (p_five / numbers) * 100
print(f"{p_one:.2f}%")
print(f"{p_two:.2f}%")
print(f"{p_three:.2f}%")
print(f"{p_four:.2f}%")
print(f"{p_five:.2f}%")
