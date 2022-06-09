from datetime import datetime

birth_year = int(input("In what year were you born?: "))
current_year = datetime.today().year

future_year = int(input("Enter a future year:"))
future_age = future_year - birth_year

print("In ",future_year," you will be ",future_age," years old.")
