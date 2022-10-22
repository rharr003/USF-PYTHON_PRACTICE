def weekday_name(day_of_week):
    weekdays = ["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if 7 > day_of_week > -1:
        return weekdays[day_of_week]
    else:
        return 'invalid range'