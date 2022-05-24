pens_price = 5.80
markers_price = 7.20
cleaner_price = 1.20

pens_amount = int(input()) * pens_price
markers_amount = int(input()) * markers_price
cleaner_amount = int(input()) * cleaner_price
discount_percentage = int(input()) / 100

needed_money = pens_amount + markers_amount + cleaner_amount
needed_money = needed_money - (needed_money * discount_percentage)
print(needed_money)
