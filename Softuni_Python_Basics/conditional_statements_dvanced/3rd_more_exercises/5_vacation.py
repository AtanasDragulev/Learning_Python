budget = float(input())
season = input()

location = ""
place_type = ""
cost = ""

if season == "Summer":
    location = "Alaska"
else:
    location = "Morocco"

if budget <= 1000:
    place_type = "Camp"
    if season == "Summer":
        cost = budget * 0.65
    else:
        cost = budget * 0.45
elif budget <= 3000:
    place_type = "Hut"
    if season == "Summer":
        cost = budget * 0.80
    else:
        cost = budget * 0.60
else:
    place_type = "Hotel"
    cost = budget * 0.90

print(f"{location} - {place_type} - {cost:.2f}")
