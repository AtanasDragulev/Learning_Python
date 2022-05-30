start_letter = input()
end_letter = input()
skipped_letter = input()
combination_counter = 0
start_to_int = ord(start_letter)
end_to_int = ord(end_letter)
skipped_letter = ord(skipped_letter)

for first_letter in range(start_to_int, end_to_int + 1):
    if first_letter != skipped_letter:
        for second_letter in range(start_to_int, end_to_int + 1):
            if second_letter != skipped_letter:
                for third_letter in range(start_to_int, end_to_int + 1):
                    if third_letter != skipped_letter:
                        print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}", end=" ")
                        combination_counter += 1
print(combination_counter)
