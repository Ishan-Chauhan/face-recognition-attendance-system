import csv
from datetime import datetime

def record_attendance(name):
    # Write the attendance to a CSV file
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    with open(current_date+'.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, datetime.now().strftime('%H:%M:%S')])
