movie_name = input()
days_screening = int(input())
tickets_amount = int(input())
ticket_price = float(input())
percentage_for_cinema = int(input())
total_income = 0

total_income += days_screening * tickets_amount * ticket_price
total_income *= 1 - percentage_for_cinema / 100
print(f"The profit from the movie {movie_name} is {total_income:.2f} lv.")