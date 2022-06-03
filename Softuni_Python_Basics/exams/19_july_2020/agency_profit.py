company_name = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_price = float(input())
agency_tax = float(input())
total_income = adult_tickets * adult_price + child_tickets * adult_price * 0.30
total_income += (adult_tickets + child_tickets) * agency_tax
total_income *= 0.20
print(f"The profit of your agency from {company_name} tickets is {total_income:.2f} lv.")
