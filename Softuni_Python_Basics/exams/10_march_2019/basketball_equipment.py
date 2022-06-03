yearly_cost = int(input())

shoes = yearly_cost * 0.6
clothes = shoes * 0.8
ball = clothes / 4
accessories = ball / 5

cost = yearly_cost + shoes + clothes + \
       ball + accessories

print(f"{cost:.2f}")