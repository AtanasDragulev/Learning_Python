period = int(input())
patients_checked = 0
patients_not_checked = 0
doctors = 7
checkup_day = 1

for day in range(period):
    current = int(input())
    if checkup_day == 3:
        if patients_not_checked > patients_checked:
            doctors += 1
        checkup_day = 0
    if current <= doctors:
        patients_checked += current
    else:
        patients_checked += doctors
        patients_not_checked += current - doctors
    checkup_day += 1

print(f"Treated patients: {patients_checked}.")
print(f"Untreated patients: {patients_not_checked}.")