from datetime import datetime, timedelta
current_date = datetime.today()
new_date = current_date - timedelta(days=5)

print("Current date:", current_date.date())
print("Date 5 days ago:", new_date.date())