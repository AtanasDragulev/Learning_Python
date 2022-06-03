first_player_name = input()
second_player_name = input()
first_player_points = 0
second_player_points = 0
first_card = input()
is_wars = False
while first_card != "End of game":
    second_card = input()
    if int(first_card) > int(second_card):
        first_player_points += int(first_card) - int(second_card)
    elif int(first_card) < int(second_card):
        second_player_points += int(second_card) - int(first_card)
    else:
        is_wars = True
        first_card = input()
        second_card = input()
        if int(first_card) > int(second_card):
            winner = first_player_name
            winner_points = first_player_points
            break
        else:
            winner = second_player_name
            winner_points = second_player_points
            break
    first_card = input()
if is_wars:
    print("Number wars!")
    print(f"{winner} is winner with {winner_points} points")
else:
    print(f"{first_player_name} has {first_player_points} points")
    print(f"{second_player_name} has {second_player_points} points")
