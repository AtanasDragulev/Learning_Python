order_amount = int(input())
frame_size = input()
delivery_type = input()
is_invalid = False
single_price = 0
total_price = 0
if order_amount < 10:
    is_invalid = True
else:
    if frame_size == "90X130":
        single_price = 110
        if order_amount > 60:
            single_price *= 0.92
        elif order_amount > 30:
            single_price *= 0.95
    elif frame_size == "100X150":
        single_price = 140
        if order_amount > 80:
            single_price *= 0.90
        elif order_amount > 40:
            single_price *= 0.94
    elif frame_size == "130X180":
        single_price = 190
        if order_amount > 50:
            single_price *= 0.88
        elif order_amount > 20:
            single_price *= 0.93
    else:
        single_price = 250
        if order_amount > 50:
            single_price *= 0.86
        elif order_amount > 25:
            single_price *= 0.91
    total_price += order_amount * single_price
    if delivery_type == "With delivery":
        total_price += 60
    if order_amount > 99:
        total_price *= 0.96
if is_invalid:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
