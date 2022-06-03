winner = ""
winner_points = 0
current_points =0
current = input()
while current != "Stop":
    for letter in current:
        number = int(input())
        if number == ord(letter):
            current_points += 10
        else:
            current_points += 2
    if current_points >= winner_points:
        winner_points = current_points
        winner = current
    current_points = 0
    current = input()
print(f"The winner is {winner} with {winner_points} points!")
