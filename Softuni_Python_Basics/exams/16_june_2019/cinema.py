places_available = int(input())
income = 0
is_full = False
while not is_full:
    current = input()
    if current == "Movie time!":
        is_full = False
        break
    if int(current) > places_available:
        is_full = True
        break
    else:
        places_available -= int(current)
        income += int(current) * 5
        if int(current) % 3 == 0:
            income -= 5
if is_full:
    print("The cinema is full.")
else:
    print(f"There are {places_available} seats left in the cinema.")
print(f"Cinema income - {income} lv.")
