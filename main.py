import pandas
from datetime import datetime
import random

data = pandas.read_csv("birthdays.csv")
today = (datetime.now().month, datetime.now().day)

new_dict = {(row.month, row.day): row for index, row in data.iterrows()}

if today in new_dict:
    birthday_person = new_dict[today]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person['name'])
        print(content)




