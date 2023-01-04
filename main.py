##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import pandas as pandas
import os, random
from topsecret import *

now = dt.datetime.now()
month_now = now.month
day_now = now.day

birthdays_data = pandas.read_csv("birthdays.csv")
birthdays_today = birthdays_data.loc[
    (birthdays_data['month'] == month_now) & (birthdays_data['day'] == day_now)].to_dict(orient="records")

if len(birthdays_today) > 0:
    for birthday_today in birthdays_today:
        file = random.choice(os.listdir("letter_templates"))

        with open(f"letter_templates/{file}") as template:
            data = template.read()
            letter = data.replace("[NAME]", birthday_today["name"])

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=birthday_today["email"],
        msg=f"Subject:Happy birthday!\n\n{letter}"
    )
