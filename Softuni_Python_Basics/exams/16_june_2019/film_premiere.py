john_wick = {"Drink": 12, "Popcorn": 15, "Menu": 19}
star_wars = {"Drink": 18, "Popcorn": 25, "Menu": 30}
jumanji = {"Drink": 9, "Popcorn": 11, "Menu": 14}
total_cost = 0
movie_name = input()
package_type = input()
ticket_amount = int(input())

if movie_name == "John Wick":
    total_cost += john_wick[package_type] * ticket_amount
elif movie_name == "Star Wars":
    total_cost += star_wars[package_type] * ticket_amount
    if ticket_amount >= 4:
        total_cost *= 0.70
else:
    total_cost += jumanji[package_type] * ticket_amount
    if ticket_amount == 2:
        total_cost *= 0.85

print(f"Your bill is {total_cost:.2f} leva.")
