from datetime import datetime
date1 = datetime(2024, 2, 10, 14, 30, 0)  
date2 = datetime(2024, 2, 15, 18, 45, 0)  

difference = abs((date2 - date1).total_seconds())

print("Difference:", difference)