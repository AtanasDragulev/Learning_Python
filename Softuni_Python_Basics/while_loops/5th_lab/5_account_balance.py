account_amount = 0
current = input()

while current != "NoMoreMoney":
    to_add = float(current)
    if to_add < 0:
        print("Invalid operation!")
        break
    else:
        account_amount += to_add
        print(f"Increase: {to_add:.2f}")
    current = input()

print(f"Total: {account_amount:.2f}")
