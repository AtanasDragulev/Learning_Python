sold_games = int(input())
hearthstone = 0
fortnite = 0
overwatch = 0
others = 0
for game in range(sold_games):
    current_game = input()
    if current_game == "Hearthstone":
        hearthstone += 1
    elif current_game == "Fornite":
        fortnite += 1
    elif current_game == "Overwatch":
        overwatch += 1
    else:
        others += 1
hearthstone = hearthstone / sold_games * 100
fortnite = fortnite / sold_games * 100
overwatch = overwatch / sold_games * 100
others = others / sold_games * 100
print(f"Hearthstone - {hearthstone:.2f}%")
print(f"Fornite - {fortnite:.2f}%")
print(f"Overwatch - {overwatch:.2f}%")
print(f"Others - {others:.2f}%")
