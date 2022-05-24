vegetable_price_kg = float(input())
fruit_price_kg = float(input())
vegetable_amount = int(input())
fruit_amount = int(input())

sales_bgn = vegetable_amount * vegetable_price_kg + \
            fruit_amount * fruit_price_kg

sales_euro = sales_bgn / 1.94

print(f'{sales_euro:.2f}')
