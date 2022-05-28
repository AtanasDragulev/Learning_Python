duration = int(input())
room_type = input()
score = input()

duration -= 1
price = 0
discount = 0

if room_type == "room for one person":
    price = duration * 18.00
elif room_type == "apartment":
    price = duration * 25.00
    if duration < 10:
        discount = price * 0.30
    elif duration <= 15:
        discount = price * 0.35
    else:
        discount = price * 0.50
else:
    price = duration * 35.00
    if duration < 10:
        discount = price * 0.10
    elif duration <= 15:
        discount = price * 0.15
    else:
        discount = price * 0.20

if score == "positive":
    price = (price - discount) * 1.25
else:
    price = (price - discount) * 0.90

print(f"{price:.2f}")
