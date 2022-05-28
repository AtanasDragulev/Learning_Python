num_of_orders = int(input())
total = 0
price = 0

for i in range(num_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())

    price = (capsule_price * capsules_per_day) * days
    total += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")

