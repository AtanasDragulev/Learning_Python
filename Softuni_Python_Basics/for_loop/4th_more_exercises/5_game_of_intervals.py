moves = int(input())
to_nine = 0
to_nineteen = 0
to_twenty_nine = 0
to_thirty_nine = 0
to_fifty = 0
invalids = 0
total_score = 0

for i in range(moves):
    current = int(input())
    if 0 <= current <= 9:
        total_score += current * 0.20
        to_nine += 1
    elif 10 <= current <= 19:
        total_score += current * 0.30
        to_nineteen += 1
    elif 20 <= current <= 29:
        total_score += current * 0.40
        to_twenty_nine += 1
    elif 30 <= current <= 39:
        total_score += 50
        to_thirty_nine += 1
    elif 40 <= current <= 50:
        total_score += 100
        to_fifty += 1
    else:
        total_score /= 2
        invalids += 1

to_nine = to_nine / moves * 100
to_nineteen = to_nineteen / moves * 100
to_twenty_nine = to_twenty_nine / moves * 100
to_thirty_nine = to_thirty_nine / moves * 100
to_fifty = to_fifty / moves * 100
invalids = invalids / moves * 100

print(f"{total_score:.2f}")
print(f"From 0 to 9: {to_nine:.2f}%")
print(f"From 10 to 19: {to_nineteen:.2f}%")
print(f"From 20 to 29: {to_twenty_nine:.2f}%")
print(f"From 30 to 39: {to_thirty_nine:.2f}%")
print(f"From 40 to 50: {to_fifty:.2f}%")
print(f"Invalid numbers: {invalids:.2f}%")
