gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

fuel_type = input()
fuel_amount = float(input())
club_card = input()
fuel_type = fuel_type.lower()
club_card = club_card.lower()
discount = 0
fuel_cost = 0

if fuel_type == "gas":
    fuel_cost = fuel_amount * gas_price
    discount = 0.08
elif fuel_type == "gasoline":
    fuel_cost = fuel_amount * gasoline_price
    discount = 0.18
elif fuel_type == "diesel":
    fuel_cost = fuel_amount * diesel_price
    discount = 0.12

if club_card == "yes":
    fuel_cost -= fuel_amount * discount

if 20 <= fuel_amount <= 25:
    fuel_cost *= 0.92
if fuel_amount > 25:
    fuel_cost *= 0.90

print(f'{fuel_cost:.2f} lv.')