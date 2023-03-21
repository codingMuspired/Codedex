#main.py

#continuation of creating our own modules by implementing created module

import datetime, bday_messages

today = datetime.date.today()
my_next_birthday = datetime.date(2023, 6, 16)

days_away = my_next_birthday - today

if (today == my_next_birthday):
    print(bday_messages.random_message)

else:
    print(f'My next birthday is {days_away} away from today! 🎂')
