# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

#Days
days_lived = age * 365
ninety_years_in_days = 90 * 365
days_left = ninety_years_in_days - days_lived
#Weeks
ninety_years_in_weeks = 90 * 52
weeks_lived = age * 52
weeks_left = ninety_years_in_weeks - weeks_lived
#Months
ninety_years_in_months = 90 * 12
months_lived = age * 12
months_left = ninety_years_in_months - months_lived

#You have x days, y weeks, and z months left.

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")




