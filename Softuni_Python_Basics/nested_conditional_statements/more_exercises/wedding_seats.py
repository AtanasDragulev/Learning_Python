last_sector = input()
rows_first_sector = int(input())
seats_odd_row = int(input())
seat_counter = 0

for sector in range(ord("A"), ord(last_sector)+1):
    for row in range(1, rows_first_sector+1):
        current_seats = seats_odd_row
        if row % 2 == 0:
            current_seats += 2
        for seat in range(1,current_seats +1):
            print(f"{chr(sector)}{row}{chr(96+seat)}")
            seat_counter += 1
    rows_first_sector += 1

print(seat_counter)