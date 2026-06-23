import calendar

def print_calendar_range():
    year= int(input("Enter the year: "))
    start_month = input("Enter start month (name or number): ")
    end_month = input("Enter end month (name or number): ")


    if start_month.isdigit() or end_month.isdigit():
    month = int(start_month) or int(end_month)
    
    else:
    month_name = start_month.capitalize() and end_month.capitalize()
    month_list = list(calendar.month_name)
    month = month_list.index(month_name)
    
print("Here's your calendar:")
print(calendar.month(year, month))