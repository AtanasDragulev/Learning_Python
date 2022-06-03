budget = float(input())
people = int(input())
clothes_cost = float(input())

decor = budget * 0.10
clothes_cost *= people

if people > 150:
    clothes_cost *= 0.90

total_cost = decor + clothes_cost
difference = abs(budget - total_cost)

if budget < total_cost:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
    