from datetime import datetime, timedelta






now_date = datetime.now()
result_date = now_date - timedelta(days=5)

print("Результат после вычитания пяти дней:", drop_microseconds(result_date))



today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера: ", drop_microseconds(yesterday))
print("Сегодня: ", drop_microseconds(today))
print("Завтра: ", drop_microseconds(tomorrow))

print("Разница между вчерашним и завтрешним в секундах: ", calculate_time_seconds(yesterday, tomorrow))



def drop_microseconds(date_mic):
    return date_mic.strftime("%Y-%m-%d %H-%M-%S")




def calculate_time_seconds(dat1, dat2):
    time_difference = dat2 - dat1
    return time_difference.total_seconds()