page_price = float(input())
cover_price = float(input())
discount_percent = int(input())
designer_price = float(input())
team_percent = int(input())

discount_percent = 1 - discount_percent / 100
team_percent = 1 - team_percent / 100
sum_needed = page_price * 899 + cover_price * 2
sum_needed *= discount_percent
sum_needed += designer_price
sum_needed *= team_percent

print(f"Avtonom should pay {sum_needed:.2f} BGN.")
