food_bough = int(input())
food_bough *= 1000
food_eaten = 0
is_eaten = False

current = input()
while current != "Adopted":
    food_eaten += int(current)
    current = input()
if food_bough < food_eaten:
    is_eaten = True

difference = abs(food_bough - food_eaten)
if is_eaten:
    print(f"Food is not enough. You need {difference} grams more.")
else:
    print(f"Food is enough! Leftovers: {difference} grams.")