maximum_male = int(input())
maximum_female = int(input())
maximum_tables = int(input())
tables_used = 0

for male in range(1, maximum_male +1):
    for female in range(1, maximum_female+1):
        if tables_used < maximum_tables:
            print(f"({male} <-> {female})", end=" ")
            tables_used += 1
