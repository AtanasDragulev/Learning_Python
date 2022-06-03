balls_amount = int(input())
total_point = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
other_counter = 0
black_counter = 0

for ball in range(balls_amount):
    current = input()
    if current == "red":
        red_counter += 1
        total_point += 5
    elif current == "orange":
        orange_counter += 1
        total_point += 10
    elif current == "yellow":
        yellow_counter += 1
        total_point += 15
    elif current == "white":
        white_counter += 1
        total_point += 20
    elif current == "black":
        black_counter += 1
        total_point = int(total_point / 2)
    else:
        other_counter += 1
print(f"Total points: {total_point}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {other_counter}")
print(f"Divides from black balls: {black_counter}")
