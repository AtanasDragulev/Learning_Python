season = input()
km_monthly = float(input())

salary = 0

if km_monthly <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = km_monthly * 0.75 * 4
    elif season == "Summer":
        salary = km_monthly * 0.90 * 4
    else:
        salary = km_monthly * 1.05 * 4
elif km_monthly <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = km_monthly * 0.95 * 4
    elif season == "Summer":
        salary = km_monthly * 1.10 * 4
    else:
        salary = km_monthly * 1.25 * 4
elif km_monthly <= 20000:
    salary = km_monthly * 1.45 * 4

salary *= 0.90

print(f'{salary:.2f}')
