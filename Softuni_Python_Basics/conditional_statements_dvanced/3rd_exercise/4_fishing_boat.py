budget = int(input())
season = input()
number_of_people = int(input())

ship_rent = 0

if season == "Spring":
    ship_rent = 3000
elif season == "Winter":
    ship_rent = 2600
else:
    ship_rent = 4200

if number_of_people <= 6:
    ship_rent *= 0.90
elif number_of_people <= 11:
    ship_rent *= 0.85
else:
    ship_rent *= 0.75

if number_of_people % 2 == 0 and season != "Autumn":
    ship_rent *= 0.95

difference = abs(ship_rent - budget)

if ship_rent <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
