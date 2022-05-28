budget = float(input())
season = input()

place_to_stay = ""
expense = 0
destination = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_to_stay = "Camp"
        expense = budget * 0.30
    else:
        place_to_stay = "Hotel"
        expense = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place_to_stay = "Camp"
        expense = budget * 0.40
    else:
        place_to_stay = "Hotel"
        expense = budget * 0.80
else:
    destination = "Europe"
    place_to_stay = "Hotel"
    expense = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place_to_stay} - {expense:.2f}")
