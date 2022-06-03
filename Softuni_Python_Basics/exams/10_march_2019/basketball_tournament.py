game_counter = 0
won_counter = 0
lost_counter = 0
tournament_name = input()
while tournament_name != "End of tournaments":
    tournament_matches = int(input())
    game_counter += tournament_matches
    for match in range(1, tournament_matches + 1):
        our_score = int(input())
        opponent_score = int(input())
        difference = abs(our_score - opponent_score)
        if our_score > opponent_score:
            won_counter += 1
            print(f"Game {match} of tournament {tournament_name}: win with {difference} points.")
        elif our_score < opponent_score:
            lost_counter += 1
            print(f"Game {match} of tournament {tournament_name}: lost with {difference} points.")
    tournament_name = input()

won_counter = (won_counter / game_counter) * 100
lost_counter = 100 - won_counter
print(f"{won_counter:.2f}% matches win")
print(f"{lost_counter:.2f}% matches lost")
