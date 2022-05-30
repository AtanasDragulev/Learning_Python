movie_title = ""
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
ticket_type = ""
places_used = 0

while movie_title != "Finish":
    movie_title = input()

    if movie_title == "Finish":
        break

    places_free = int(input())
    places_used = 0
    ticket_type = ""
    while places_free > places_used and ticket_type != "End":
        ticket_type = input()
        if ticket_type == "End" or ticket_type == "Finish" or places_used == places_free:
            break
        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        places_used += 1
        total_tickets += 1

    percent_full = (places_used / places_free) * 100
    print(f"{movie_title} - {percent_full:.2f}% full.")


student_percentage = (student_tickets / total_tickets) * 100
standard_percentage = (standard_tickets / total_tickets) * 100
kid_percentage = (kid_tickets/ total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kid_percentage:.2f}% kids tickets.")
