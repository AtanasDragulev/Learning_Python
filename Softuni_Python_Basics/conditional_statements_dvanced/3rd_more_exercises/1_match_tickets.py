budget = float(input())
ticket_type = input()
people = int(input())

ticket_price = 0

if ticket_type == "VIP":
    ticket_price = 499.99
else:
    ticket_price = 249.99

ticket_price *= people
travel_cost = 0

if 1 <= people <= 4:
    travel_cost = budget * 0.75
elif 5 <= people <= 9:
    travel_cost = budget * 0.60
elif 10 <= people <= 24:
    travel_cost = budget * 0.50
elif 25 <= people <= 49:
    travel_cost = budget * 0.40
else:
    travel_cost = budget * 0.25

needed = travel_cost + ticket_price
difference = abs(budget - needed)

if budget >= needed:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
