print('Focus Timer')
print('Please input focus time (minutes):')
focus_time = int(input()) 
start_time = time.time() 
end_time = start_time + focus_time * 60  
while time.time() < end_time:
    current_time = end_time - time.time()
    m, s = divmod(current_time, 60)
    print(f'\r{m:02d}:{s:02d}', end='') 
    time.sleep(1)
print('\nFocus time end!')
