budget = float(input())
season = input()

cost = 0
car_class = ""
car_type = ""

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        cost = budget * 0.35
        car_type = "Cabrio"
    else:
        cost = budget * 0.65
        car_type = "Jeep"
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        cost = budget * 0.45
        car_type = "Cabrio"
    else:
        cost = budget * 0.80
        car_type = "Jeep"
else:
    cost = budget * 0.90
    car_class = "Luxury class"
    car_type = "Jeep"

print(car_class)
print(f'{car_type} - {cost:.2f}')
