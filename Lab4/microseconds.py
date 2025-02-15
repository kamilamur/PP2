from datetime import datetime
now = datetime.now()
new_now = now.replace(microsecond=0)
print("With:", now)
print("Without:", new_now)