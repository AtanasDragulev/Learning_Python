best_player = ""
best_scored = 0
is_hat_trick = False
while True:
    current_player = input()
    if current_player == "END":
        break
    current_score = int(input())
    if current_score > best_scored:
        best_scored = current_score
        best_player = current_player
        if best_scored >= 3:
            is_hat_trick = True
    if current_score >= 10:
        break
print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {best_scored} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_scored} goals.")
