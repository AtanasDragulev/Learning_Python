secret_message = ""
is_c_met = False
is_o_met = False
is_n_met = False

while True:
    if is_c_met and is_o_met and is_n_met:
        is_c_met = False
        is_o_met = False
        is_n_met = False
        print(secret_message, end= " ")
        secret_message = ""

    letter = input()
    if letter == "End":
        break

    if letter.isalpha():
        if letter == "c" and not is_c_met:
            is_c_met = True
            continue
        elif letter == "o" and not is_o_met:
            is_o_met = True
            continue
        elif letter == "n" and not is_n_met:
            is_n_met = True
            continue
        secret_message += letter
    else:
        continue
