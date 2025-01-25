import datetime
import random

dates = []

for i in range(10):
    year = random.randint(2000, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    dates.append(datetime.date(year, month, day))