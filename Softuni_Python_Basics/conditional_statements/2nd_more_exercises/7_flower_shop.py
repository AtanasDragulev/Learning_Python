import math

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

magnolia = int(input())
hyacinth = int(input())
rose = int(input())
cactus = int(input())
gift_price = float(input())

total = magnolia * magnolia_price + hyacinth * hyacinth_price + \
    rose * rose_price + cactus * cactus_price
total *= 0.95
difference = abs(total - gift_price)

if total >= gift_price:
    difference = math.floor(difference)
    print(f'She is left with {difference} leva.')
else:
    difference = math.ceil(difference)
    print(f'She will have to borrow {difference} leva.')
    