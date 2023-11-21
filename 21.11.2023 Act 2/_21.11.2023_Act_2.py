def convert_age(Age):
    days= 365*Age
    hours = days * 24
    return days, hours

days, hours = convert_age(12)
print(days)
print(hours)