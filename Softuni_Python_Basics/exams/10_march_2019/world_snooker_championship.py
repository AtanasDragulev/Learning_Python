tournament_stage = input()
ticket_type = input()
ticket_amount = int(input())
with_photo = input()
total_cost = 0
ticket_price = 0

if tournament_stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    else:
        ticket_price = 118.90
elif tournament_stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    else:
        ticket_price = 300.40
else:
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    else:
        ticket_price = 400
total_cost = ticket_price * ticket_amount
if total_cost > 4000:
    total_cost *= 0.75
    with_photo = "N"
elif total_cost > 2500:
    total_cost *= 0.90
if with_photo == "Y":
    total_cost += ticket_amount * 40
print(f"{total_cost:.2f}")