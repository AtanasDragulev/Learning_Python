visitors_amount = int(input())
back_training = 0
chest_training = 0
legs_training = 0
abs_training = 0
protein_shake = 0
protein_bar = 0
for visitor in range(visitors_amount):
    current = input()
    if current == "Back":
        back_training += 1
    elif current == "Chest":
        chest_training += 1
    elif current == "Legs":
        legs_training += 1
    elif current == "Abs":
        abs_training += 1
    elif current == "Protein shake":
        protein_shake += 1
    elif current == "Protein bar":
        protein_bar += 1

people_training = ((back_training + chest_training + legs_training + abs_training) / visitors_amount) * 100
people_buying = 100 - people_training
print(f"{back_training} - back")
print(f"{chest_training} - chest")
print(f"{legs_training} - legs")
print(f"{abs_training} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{people_training:.2f}% - work out")
print(f"{people_buying:.2f}% - protein")
