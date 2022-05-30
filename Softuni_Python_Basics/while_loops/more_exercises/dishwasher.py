detergent = int(input())
detergent *= 750
clean_dishes = 0
clean_pots = 0
wash_counter = 1
per_item = 0
is_out_of_detergent = False
current = input()

while current != "End":
    items = int(current)
    if wash_counter % 3 == 0:
        per_item = 15
        clean_pots += items
    else:
        per_item = 5
        clean_dishes += items
    detergent -= items * per_item
    if detergent < 0:
        is_out_of_detergent = True
        break
    wash_counter += 1
    current = input()

detergent = abs(detergent)
if is_out_of_detergent:
    print(f"Not enough detergent, {detergent} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")
