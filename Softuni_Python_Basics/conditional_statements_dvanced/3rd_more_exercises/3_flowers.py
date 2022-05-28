chrysanthemum_amount = int(input())
roses_amount = int(input())
tulips_amount = int(input())
season = input()
holiday = input()

total = 0

if season == 'Spring' or season == 'Summer':
    total = chrysanthemum_amount * 2.00 + roses_amount * 4.10 + tulips_amount * 2.50
    if holiday == 'Y':
        total *= 1.15
else:
    total = chrysanthemum_amount * 3.75 + roses_amount * 4.50 + tulips_amount * 4.15
    if holiday == "Y":
        total *= 1.15

if tulips_amount > 7 and season == "Spring":
    total *= 0.95
if roses_amount >= 10 and season == "Winter":
    total *= 0.90
if chrysanthemum_amount + roses_amount + tulips_amount > 20:
    total *= 0.80

total += 2
print(f"{total:.2f}")
