ticket_type = input()
rows = int(input())
columns = int(input())

number_of_seats = rows * columns
sales = 0

if ticket_type == "Premiere":
    sales = number_of_seats * 12.00
elif ticket_type == "Normal":
    sales = number_of_seats * 7.50
elif ticket_type == "Discount":
    sales = number_of_seats * 5.00

print(f"{sales:.2f} leva")