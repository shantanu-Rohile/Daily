# 2. Person Class with Age Calculation

from datetime import datetime

class Prson_Age:
    def __init__(self,name,month,year):
        self.month = month
        self.year = year
        self.name = name

    def calculate_age(self):
        current_date = datetime.now()

        current_year  =  current_date.year
        current_month = current_date.month

        print(f"Mr./Mrs. {self.name} is {current_year - self.year} year and {current_month-self.month} months old")



name = input("Please Enter your name : ")
year = int(input("Please Enter your birth year : "))
month = int(input("Please Enter your birth month : "))
# day = int(input("Please Enter your birth day : "))

p1 = Prson_Age(name,month,year)

p1.calculate_age()