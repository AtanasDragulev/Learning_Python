target_height = int(input())
current_height = target_height - 30
jump_counter = 0
failed_jump = 0
is_failed = False

while not is_failed:
    current_jump = int(input())
    jump_counter += 1
    if current_jump <= current_height:
        failed_jump += 1
        if failed_jump == 3:
            is_failed = True
    else:
        if current_height >= target_height:
            break
        current_height += 5
        failed_jump = 0


if is_failed:
    print(f"Tihomir failed at {current_height}cm after {jump_counter} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {jump_counter} jumps.")
