fuel_type = input()
fuel_amount = int(input())
fuel_type = fuel_type.lower()

if fuel_type == 'diesel' or fuel_type == 'gasoline' or fuel_type == "gas":
    if fuel_amount >= 25:
        print(f'You have enough {fuel_type}.')
    else:
        print(f'Fill your tank with {fuel_type}!')
else:
    print(f'Invalid fuel!')
