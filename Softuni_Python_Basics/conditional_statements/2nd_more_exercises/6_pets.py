import math
days = int(input())
food_available = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

dog_food *= days
cat_food *= days
turtle_food *= days / 1000

food_needed = dog_food + cat_food + turtle_food
difference = abs(food_needed - food_available)

if food_needed <= food_available:
    difference = math.floor(difference)
    print(f'{difference} kilos of food left.')
else:
    difference = math.ceil(difference)
    print(f'{difference} more kilos of food are needed.')
