tabs_amount = int(input())
salary = int(input())

for i in range(tabs_amount):
    current_site = input()
    if current_site == "Facebook":
        salary -= 150
    elif current_site == "Instagram":
        salary -= 100
    elif current_site == "Reddit":
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
    