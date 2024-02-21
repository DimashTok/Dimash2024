#Write a Python program to print yesterday, today, tomorrow.

import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
Tomorrow = today + datetime.timedelta(days=1)
print(f"yesterday: {yesterday.strftime('%A')}")
print(f"today: {today.strftime('%A')}")
print(f"Tomorrow: {Tomorrow.strftime('%A')}")