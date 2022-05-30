number = int(input())

for first in range(1,10):
    for second in range(1,10):
        for third in range(1,10):
            for forth in range(1,10):
                if first + second == third + forth:
                    if number % (first + second) == 0:
                        print(f"{first}{second}{third}{forth}", end=" ")