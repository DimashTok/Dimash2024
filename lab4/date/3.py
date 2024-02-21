#Write a Python program to drop microseconds from datetime.

import datetime
today = datetime.datetime.now()
print(today.strftime('%Y/%m/%d %H:%M:%S'))