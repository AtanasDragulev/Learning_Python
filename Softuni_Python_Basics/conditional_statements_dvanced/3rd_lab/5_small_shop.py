item = input()
city = input()
amount = float(input())

sofia = {"coffee": 0.50, "water": 0.80, "beer": 1.20, "sweets": 1.45, "peanuts": 1.60}
plovdiv = {"coffee": 0.40, "water": 0.70, "beer": 1.15, "sweets": 1.30, "peanuts": 1.50}
varna = {"coffee": 0.45, "water": 0.70, "beer": 1.10, "sweets": 1.35, "peanuts": 1.55}

if city == "Sofia":
    total = amount * sofia[item]
    print(total)
elif city == "Plovdiv":
    total = amount * plovdiv[item]
    print(total)
else:
    total = amount * varna[item]
    print(total)
