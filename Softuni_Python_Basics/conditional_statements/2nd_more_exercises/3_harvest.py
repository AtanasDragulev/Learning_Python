import math

vineyard_area = int(input())
grapes_per_sqm = float(input())
needed_wine = int(input())
workers = int(input())

wine_to_make = ((vineyard_area * grapes_per_sqm) * 0.4) / 2.5
difference = abs(needed_wine - wine_to_make)

if wine_to_make < needed_wine:
    difference = math.floor(difference)
    print(f'It will be a tough winter! More {difference} liters wine needed.')
else:
    wine_to_make = math.floor(wine_to_make)
    difference = math.ceil(difference)
    wine_per_worker = math.ceil(difference / workers)

    print(f'Good harvest this year! Total wine: {wine_to_make} liters.')
    print(f'{difference} liters left -> {wine_per_worker} liters per person.')
