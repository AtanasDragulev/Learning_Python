expected_money = int(input())
cash_amount = 0
card_amount = 0
cash_payments = 0
card_payments = 0
is_collected = False
item_counter = 0
current = input()


while current != "End":
    current_cash = int(current)
    if item_counter % 2 == 0 and current_cash <= 100:        # Cash and price under 100
        cash_amount += current_cash
        cash_payments += 1
        print("Product sold!")
    elif item_counter % 2 != 0 and current_cash >= 10:       # Card and price over 10
        card_amount += current_cash
        card_payments += 1
        print("Product sold!")
    else:                                                   # Invalid payment
        print("Error in transaction!")
    if cash_amount + card_amount >= expected_money:
        is_collected = True
        break
    item_counter += 1
    current = input()

if is_collected:
    if cash_payments == 0:
        average_cash = 0
    else:
        average_cash = cash_amount / cash_payments
    if card_payments == 0:
        average_card = 0
    else:
        average_card = card_amount / card_payments
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")
else:
    print("Failed to collect required money for charity.")
