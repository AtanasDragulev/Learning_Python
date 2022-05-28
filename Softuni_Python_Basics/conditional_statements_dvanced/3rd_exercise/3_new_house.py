flower_type = input()
flower_amount = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    if flower_amount > 80:
        price = flower_amount * 5 * 0.90
    else:
        price = flower_amount * 5
elif flower_type == "Dahlias":
    if flower_amount > 90:
        price = flower_amount * 3.80 * 0.85
    else:
        price = flower_amount * 3.80
elif flower_type == "Tulips":
    if flower_amount > 80:
        price = flower_amount * 2.80 * 0.85
    else:
        price = flower_amount * 2.80
elif flower_type == "Narcissus":
    if flower_amount < 120:
        price = flower_amount * 3.00 * 1.15
    else:
        price = flower_amount * 3.00
else:                                   #Gladiolus
    if flower_amount < 80:
        price = flower_amount * 2.50 * 1.2
    else:
        price = flower_amount * 2.50

difference = abs(budget - price)

if price <= budget:
    print(f"Hey, you have a great garden with {flower_amount} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
