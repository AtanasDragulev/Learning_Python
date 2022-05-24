deposit = float(input())
srok = int(input())
lihven_procent = float(input())/100

suma = deposit + srok*((deposit*lihven_procent)/12)

print(suma)
