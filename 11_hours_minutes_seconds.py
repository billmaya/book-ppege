# Exercise 11 - Hours Minutes Seconds

def getHoursMinutesSeconds(totalSeconds):
   
    verbose = True

    hours = 0
    minutes = 0
    seconds = totalSeconds

    secondsPerHour = 3600
    secondsPerMinute = 60

    # Calculate hours, minutes, and seconds
    if totalSeconds == 0:
        if verbose:
            print(f'{totalSeconds} SECONDS DISPLAYED AS 0s')
        return '0s'

    hours = seconds // secondsPerHour
    if hours != 0:
        seconds -= (hours * secondsPerHour)

    minutes = seconds // secondsPerMinute
    if minutes != 0: 
        seconds -= (minutes * secondsPerMinute)

    # Format the final string
    hms = []

    if hours != 0:
        hms.append(str(hours) + 'h')

    if minutes != 0:
        hms.append(str(minutes) + 'm')

    if seconds != 0:
        hms.append(str(seconds) + 's')

    if verbose:
        print(f"{totalSeconds} SECONDS DISPLAYED AS {' '.join(hms)}")

    return ' '.join(hms)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
