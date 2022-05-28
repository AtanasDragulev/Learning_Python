month = input()
days = int(input())

studio_cost = 0
apartment_cost = 0

if month == "May" or month == "October":
    studio_cost = days * 50
    apartment_cost = days * 65
    if 7 < days < 14:
        studio_cost *= 0.95
    elif days > 14:
        studio_cost *= 0.70
elif month == "June" or month == "September":
    studio_cost = days * 75.20
    apartment_cost = days * 68.70
    if days > 14:
        studio_cost *= 0.80
else:
    studio_cost = days * 76
    apartment_cost = days * 77

if days > 14:
    apartment_cost *= 0.90

print(f"Apartment: {apartment_cost:.2f} lv.")
print(f"Studio: {studio_cost:.2f} lv.")
