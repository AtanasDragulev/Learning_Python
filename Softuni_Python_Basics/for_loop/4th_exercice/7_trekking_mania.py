trekkers = int(input())
musala = 0
monblan = 0
kiliman = 0
k_two = 0
everest = 0
total_trekkers = 0


for i in range(trekkers):
    current = int(input())
    total_trekkers += current
    if current <= 5:
        musala += current
    elif current <= 12:
        monblan += current
    elif current <= 25:
        kiliman += current
    elif current <= 40:
        k_two += current
    else:
        everest += current

musala = (musala / total_trekkers) * 100
monblan = (monblan / total_trekkers) * 100
kiliman = (kiliman / total_trekkers) * 100
k_two = (k_two / total_trekkers) * 100
everest = (everest / total_trekkers) * 100
print(f"{musala:.2f}%")
print(f"{monblan:.2f}%")
print(f"{kiliman:.2f}%")
print(f"{k_two:.2f}%")
print(f"{everest:.2f}%")
