from datetime import date

# User input
year = int(input("Birth year nakho: "))
month = int(input("Birth month nakho (1-12): "))
day = int(input("Birth day nakho: "))

birth_date = date(year, month, day)
today = date.today()

# Age calculation
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    days += 30   # approx days

if months < 0:
    years -= 1
    months += 12

print("Tamari age chhe:")
print(years, "Years", months, "Months", days, "Days")
