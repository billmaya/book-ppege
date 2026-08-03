# Exercise 24 - Every 15 Minutes

for h in range(24):
    meridiem = 'am' if h < 12 else 'pm'
    hour = (h % 12) or 12
    for minute in range(0, 46, 15):
        print(f'{hour}:{minute:02d} {meridiem}')



