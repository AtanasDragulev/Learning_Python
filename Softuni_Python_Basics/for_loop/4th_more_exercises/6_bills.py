months = int(input())
electricity = 0
water = 0
internet = 0
others = 0

for i in range(months):
    current = float(input())
    electricity += current

water = months * 20
internet = months * 15
others = (electricity + water + internet) * 1.2
average = (electricity + water + internet + others) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")
