#Write a Python program to calculate two date difference in seconds.

import datetime
def second(date1, date2):
    if not isinstance(date1, datetime.datetime):
        date1 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    if not isinstance(date2, datetime.datetime):
        date2 = datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    difference = abs((date2 - date1).total_seconds())
    return difference
data1 = input("First date in the form:'YYYY-MM-DD HH:MM:SS':")
data2 = input("Second date in the form:'YYYY-MM-DD HH:MM:SS':")
dif = second(data1, data2)
print(f"difference between {data1} and {data2} is : {dif} seconds")