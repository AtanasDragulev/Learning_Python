team_name = input()
matches_played = int(input())
wins = 0
draws = 0
loses = 0
total_points = 0
for game in range(matches_played):
    current_result = input()
    if current_result == "W":
        wins += 1
    elif current_result == "D":
        draws += 1
    else:
        loses += 1
if matches_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    total_points = wins * 3 + draws
    win_rate = wins / matches_played * 100
    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {win_rate:.2f}%")
