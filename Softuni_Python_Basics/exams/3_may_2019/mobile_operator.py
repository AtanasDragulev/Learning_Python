contract_period = input()
contract_type = input()
added_internet = input()
months_to_pay = int(input())
monthly_price = 0
total_cost = 0

if contract_type == "Small":
    if contract_period == "one":
        monthly_price = 9.98
    else:
        monthly_price = 8.58
elif contract_type == "Middle":
    if contract_period == "one":
        monthly_price = 18.99
    else:
        monthly_price = 17.09
elif contract_type == "Large":
    if contract_period == "one":
        monthly_price = 25.98
    else:
        monthly_price = 23.59
else:
    if contract_period == "one":
        monthly_price = 35.99
    else:
        monthly_price = 31.79

if added_internet == "yes":
    if monthly_price <= 10:
        monthly_price += 5.50
    elif monthly_price <= 30:
        monthly_price += 4.35
    else:
        monthly_price += 3.85

total_cost = monthly_price * months_to_pay
if contract_period == "two":
    total_cost *= 0.9625
print(f"{total_cost:.2f} lv.")
