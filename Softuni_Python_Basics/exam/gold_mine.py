locations = int(input())
for mine in range(locations):
    expected_average = float(input())
    days_mined = int(input())
    expected_average *= 1000    # kilogram to gram
    this_mine = 0
    for day in range(days_mined):
        current_mined = float(input())
        this_mine += current_mined * 1000
    average = (this_mine / days_mined) / 1000
    if expected_average <= average * 1000:
        print(f"Good job! Average gold per day: {average:.2f}.")
    else:
        print(f"You need {(expected_average / 1000 - average):.2f} gold.")
