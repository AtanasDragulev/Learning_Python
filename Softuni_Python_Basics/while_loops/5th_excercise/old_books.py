book_name = input()
is_found = False
books_checked = 0
current = input()
while current != "No More Books":
    if current == book_name:
        is_found = True
        break
    books_checked += 1
    current = input()

if is_found:
    print(f"You checked {books_checked} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")
