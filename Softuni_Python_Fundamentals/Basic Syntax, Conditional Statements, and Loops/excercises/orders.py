orders = int(input())
total_price = 0

for order in range(orders):
    current_price = 0
    capsule_price = float(input())
    days = int(input())
    capsule_count = int(input())
    if not 0.01 <= capsule_price <= 100:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsule_count <= 2000:
        continue

    current_price += capsule_price * capsule_count * days
    total_price += current_price
    print(f"The price for the coffee is: ${current_price:.2f}")

print(f"Total: ${total_price:.2f}")
