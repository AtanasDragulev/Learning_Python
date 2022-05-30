amount_of_ones = int(input())
amount_of_twos = int(input())
amount_of_fives = int(input())
total_amount = int(input())
current = 0

for ones in range(amount_of_ones+1):
    for twos in range(amount_of_twos+1):
        for fives in range(amount_of_fives+1):
            current = ones * 1 + twos * 2 + fives * 5
            if current > total_amount:
                break
            if current == total_amount:
                print(f"{ones} * 1 lv. + {twos} * 2 lv. + {fives} * 5 lv. = {total_amount} lv.")
