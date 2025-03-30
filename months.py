import calendar

def show_months():
    months = list(calendar.month_name)[1:]  # Get month names (excluding empty first element)
    
    print("Here are all the months of the year:")
    for month in months:
        print(month)

show_months()
