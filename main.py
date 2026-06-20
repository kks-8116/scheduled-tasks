
import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = "shreshtharaj88@gmail.com"
PASSWORD = "orkryttqcqlrerot"

now = dt.datetime.now()
curr_day = now.day
curr_month = now.month

df = pd.read_csv("birthdays.csv")
days_list = df.day.to_list()
months_list = df.month.to_list()
curr_day_indexes = [index for index, day in enumerate(days_list) if day == curr_day]
today_bdday_indexes = [index for index in curr_day_indexes if months_list[index] == curr_month]
for index in today_bdday_indexes:
    name = df.iloc[index, 0]
    to_email = df.iloc[index, 1]
    letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(letter, "r") as f:
        lines = f.readlines()
        lines[0] = lines[0].replace("[NAME]", name)
        lines[-1] = lines[-1].replace("Angela", "Shreshtha")

    #keeping track of send letters by saving them by name
    with open(f"send_letters/birthday_letter_{name}.txt", "w") as f:
        for line in lines:
            f.write(line)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject:Happy Birthday!\n\n"
                                                                       f"{"".join(lines)}")
