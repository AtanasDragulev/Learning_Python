drink_type = input()
sugar = input()
drink_amount = int(input())
total_cost = 0
drink_cost = 0

if drink_type == "Espresso":
    if sugar == "Without":
        drink_cost = 0.90
    elif sugar == "Normal":
        drink_cost = 1.00
    else:
        drink_cost = 1.20
elif drink_type == "Cappuccino":
    if sugar == "Without":
        drink_cost = 1.00
    elif sugar == "Normal":
        drink_cost = 1.20
    else:
        drink_cost = 1.60
else:
    if sugar == "Without":
        drink_cost = 0.50
    elif sugar == "Normal":
        drink_cost = 0.60
    else:
        drink_cost = 0.70
total_cost += drink_amount * drink_cost
if sugar == "Without":
    total_cost *= 0.65
if drink_type == "Espresso" and drink_amount >= 5:
    total_cost *= 0.75
if total_cost > 15:
    total_cost *= 0.80
print(f"You bought {drink_amount} cups of {drink_type} for {total_cost:.2f} lv.")
