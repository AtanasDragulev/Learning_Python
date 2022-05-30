change = float(input())
change *= 100
coins = 0

coins += int(change // 200)
change = int(change % 200)
coins += int(change // 100)
change = int(change % 100)
coins += int(change // 50)
change = int(change % 50)
coins += int(change // 20)
change = int(change % 20)
coins += int(change // 10)
change = int(change % 10)
coins += int(change // 5)
change = int(change % 5)
coins += int(change // 2)
change = int(change % 2)
coins += int(change // 1)
change = int(change % 1)

print(coins)