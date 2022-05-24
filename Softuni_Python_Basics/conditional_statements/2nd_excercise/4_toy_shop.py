puzzle_price = 2.60
talk_doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

excursion_cost = float(input())
puzzle_amount = int(input())
talk_doll_amount = int(input())
teddy_bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())

total_money = puzzle_amount * puzzle_price + \
              talk_doll_amount * talk_doll_price + \
              teddy_bear_amount * teddy_bear_price + \
              minion_amount * minion_price + \
              truck_amount * truck_price

toy_amount = puzzle_amount + talk_doll_amount + teddy_bear_amount + \
              minion_amount + truck_amount

if toy_amount >= 50:
    total_money -= total_money * 0.25

total_money *= 0.9

if total_money >= excursion_cost:
    excursion_fund = total_money - excursion_cost
    print(f'Yes! {excursion_fund:.2f} lv left.')
else:
    excursion_fund = excursion_cost - total_money
    print(f'Not enough money! {excursion_fund:.2f} lv needed.')
