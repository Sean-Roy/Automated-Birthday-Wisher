from datetime import datetime
import pandas
import random
import smtplib
from pprint import pprint

# TODO: Update the "birthday.csv" file with name, email, year, month, and day for an individual.
# TODO: Update the "letter_#.txt" files with desired message - 1 will be selected at random later.

# TODO: If you add additional letter documents in the "letter_templates" folder, increase the "n" value.
n = 3

# TODO: Use the correct smtp_pv value:
#  Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
smtp_pv = "smtp.gmail.com"

# TODO: Use the correct port if it is not gmail or your provider uses a different port.
smtp_port = 587

# TODO: Change private email/password to your own personal one.
# TODO: Password is not your email password, but your app password for gmail.
my_email = "YOUR_OWN_EMAIL@gmail.com"
my_password = "YOUR_OWN_APP_PASSWORD"

# Grab today's date:
today = datetime.now()
today_tuple = (today.month, today.day)
# print(today_tuple)

# Re-format the csv file for use:
data = pandas.read_csv("birthdays.csv")
# print(data)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# pprint(birthdays_dict)

# Check if current day matches a birthday on file:
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # print(birthday_person)

    # Prepare the message to be sent by replacing the placeholder name with the name of the individual:
    file_path = f"letter_templates/letter_{random.randint(1, n)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the birthday wish email:
    with smtplib.SMTP(smtp_pv, smtp_port, timeout=120) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
