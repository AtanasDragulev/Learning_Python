import math
tournaments = int(input())
starting_points = int(input())
wins = 0
final_points = 0

for i in range(tournaments):
    current = input()
    if current == "W":
        wins += 1
        final_points += 2000
    elif current == "F":
        final_points += 1200
    else:
        final_points += 720

average = math.floor(final_points / tournaments)
wins = wins / tournaments * 100
final_points += starting_points
print(f"Final points: {final_points}")
print(f"Average points: {average}")
print(f"{wins:.2f}%")
