stadium_capacity = int(input())
fan_amount = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for fan in range(fan_amount):
    sector = input()
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    else:
        fans_g += 1

fans_a = fans_a / fan_amount * 100
fans_b = fans_b / fan_amount * 100
fans_v = fans_v / fan_amount * 100
fans_g = fans_g / fan_amount * 100
fan_amount = fan_amount / stadium_capacity * 100

print(f"{fans_a:.2f}%")
print(f"{fans_b:.2f}%")
print(f"{fans_v:.2f}%")
print(f"{fans_g:.2f}%")
print(f"{fan_amount:.2f}%")
