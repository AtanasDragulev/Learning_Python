vga_price = 250

budget = float(input())
vga_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

vga_cost = vga_amount * vga_price
cpu_cost = cpu_amount * (vga_cost * 0.35)
ram_cost = ram_amount * (vga_cost * 0.10)

needed_money = vga_cost + cpu_cost + ram_cost

if cpu_amount < vga_amount:
    needed_money -= (needed_money * 0.15)

if needed_money <= budget:
    lv_leftover = budget - needed_money
    print(f'You have {lv_leftover:.2f} leva left!')
else:
    lv_short = needed_money - budget
    print(f'Not enough money! You need {lv_short:.2f} leva more!')