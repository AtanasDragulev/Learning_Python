player_name = input()
points = 301
successful = 0
unsuccessful = 0
is_won = False
current_sector = input()
while current_sector != "Retire":
    current_points = int(input())
    if current_sector == "Double":
        current_points *= 2
    elif current_sector == "Triple":
        current_points *= 3
    if current_points > points:
        unsuccessful += 1
    else:
        successful += 1
        points -= current_points
    if points == 0:
        is_won = True
        break
    current_sector = input()
if is_won:
    print(f"{player_name} won the leg with {successful} shots.")
else:
    print(f"{player_name} retired after {unsuccessful} unsuccessful shots.")
