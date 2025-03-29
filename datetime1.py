from datetime import date, datetime

# Calling the today function of the date class
today = date.today()
now = datetime.now()

print("Today's date is", today)
print("\nCurrent Date and time is", now)

# Printing date's components
print("\nDate components:", today.year, today.month, today.day)
