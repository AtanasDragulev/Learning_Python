control_minutes = int(input())
control_seconds = int(input())
tunnel_length = float(input())
seconds_hundred_m = int(input())
control_seconds += control_minutes * 60
total_time = 0
total_time += (seconds_hundred_m / 100) * tunnel_length
total_time -= (tunnel_length / 120) * 2.5

if total_time <= control_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    difference = abs(control_seconds - total_time)
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
