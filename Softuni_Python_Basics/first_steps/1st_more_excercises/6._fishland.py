skumria_price = float(input())
caca_price = float(input())

palamut_amount = float(input())
safrid_amount = float(input())
midi_amount = float(input())

palamut_price = palamut_amount * (skumria_price * 1.6)
safrid_price = safrid_amount * (caca_price * 1.8)
midi_price = midi_amount * 7.50

total = palamut_price + safrid_price + midi_price
total = round(total,2)
print(f'{total:.2f}')