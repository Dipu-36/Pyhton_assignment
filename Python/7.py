days = int(input("Enter number of days: "))
years = days // 365
days_remaining = days % 365
months = days_remaining // 30
weeks = (days_remaining % 30) // 7
days_left = (days_remaining % 30) % 7

print(f"{years} years, {months} months, {weeks} weeks, and {days_left} days")
