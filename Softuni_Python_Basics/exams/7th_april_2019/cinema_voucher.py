voucher_amount = int(input())
item = input()
tickets = 0
others = 0
product_type = ""

while voucher_amount > 0 and item != "End":
    product_type = ""
    if len(item) > 8:
        cost = ord(item[0]) + ord(item[1])
        product_type = "movie"
    else:
        cost = ord(item[0])


    if voucher_amount - cost >= 0:
        if product_type == "movie":
            tickets += 1
        else:
            others += 1
        item = input()
        voucher_amount -= cost
    else:
        item = "End"

print(tickets)
print(others)
