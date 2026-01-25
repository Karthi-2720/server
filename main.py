import datetime as dt
import random
import smtplib
import csv

my_email = "24r05a6704@cmrithyderabad.edu.in"
password = "blru htfq nhxf nhjl"

now = dt.datetime.now()
today = (now.month, now.day)

birthday_data = {}

with open("birthdays.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        birthday_data[(int(row["month"]), int(row["day"]))] = row

if today in birthday_data:
    person = birthday_data[today]

    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        message = letter.read().replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            my_email,
            person["email"],
            f"Subject: Advance Happy Birthday {person['name']}\n\n{message}"
        )
