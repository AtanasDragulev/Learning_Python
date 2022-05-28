temperature = int(input())
time_of_day = input()

outfit = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= temperature <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 <= temperature <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif temperature >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if 10 <= temperature <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 <= temperature <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif temperature >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
else:
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
