start = int(input())
end = int(input())

start_one = int(str(start)[0])
start_two = int(str(start)[1])
start_three = int(str(start)[2])
start_four = int(str(start)[3])

end_one = int(str(end)[0])
end_two = int(str(end)[1])
end_three = int(str(end)[2])
end_four = int(str(end)[3])

for first in range(start_one, end_one+1):
    if first % 2 == 0:
        continue
    for second in range(start_two, end_two+1):
        if second % 2 == 0:
            continue
        for third in range(start_three, end_three + 1):
            if third % 2 == 0:
                continue
            for forth in range(start_four, end_four + 1):
                if forth % 2 == 0:
                    continue
                print(f"{first}{second}{third}{forth}", end=" ")
