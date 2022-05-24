pool_volume = int(input())
pipe1_debit = int(input())
pipe2_debit = int(input())
worker_off_time = float(input())

pool_state = pipe1_debit * worker_off_time + pipe2_debit * worker_off_time

pipe1_percent = ((pipe1_debit * worker_off_time) / pool_state) * 100
pipe2_percent = ((pipe2_debit * worker_off_time) / pool_state ) * 100
fill_percent = (pool_state / pool_volume) * 100

if pool_state <= pool_volume:
    print(f'The pool is {fill_percent:.2f}% full.'
          f' Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%.')
else:
    overflow = pool_state - pool_volume
    print(f'For {worker_off_time} hours the pool overflows with {overflow:.2f} liters.')