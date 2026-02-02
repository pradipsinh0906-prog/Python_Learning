from datetime import datetime

birth_str = input("Enter your birth date & time (YYYY-MM-DD HH:MM:SS):")

birth_dt = datetime.strptime(birth_str, "%Y-%m-%d %H:%M:%S")
current_dt = datetime.now()

diff = current_dt - birth_dt

total_seconds = int(diff.total_seconds())
minutes = total_seconds // 60
hours = minutes // 60
days = diff.days
months = days // 30
years = days // 365

print("\n--- Age ---")
print("Years  :", years)
print("Months :", months)
print("Days   :", days)
print("Hours  :", hours)
print("Minutes:", minutes)
print("Seconds:", total_seconds)