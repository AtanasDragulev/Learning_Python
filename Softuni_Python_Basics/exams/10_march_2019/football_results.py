won = 0
lost = 0
draw = 0
for match in range(3):
    current = input()
    if int(current[0]) > int(current[2]):
        won += 1
    elif int(current[0]) == int(current[2]):
        draw += 1
    else:
        lost += 1
print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {draw}")