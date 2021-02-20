# File: DaysInMonth.py
# Student: Emiliano Villarreal
# UT EID: ev8559
# Course Name: CS303E
# 
# Date Created: 18/02/2021
# Date Last Modified: 81/02/2021
# Description of Program: This program will take user input of a desired month
# and year and will prin a statement ststing how many days the indicated month had in the indicated year.

#year = int(input("Enter year: "))
#month = int(input("Enter month: "))


"""def main():
    
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))
    days = 0
    #This function will calculate the appropriate number of days for each month
    def numDays():
        if month == 9 or month == 4 or month == 6 or month == 11:
            days = 30
        if month == 2:
            days = 28
        else:
            days = 31
        return print(days)
        
    #This function will give the appropriate month name for the input of the user    
    def monthName():
        if (month == 1):
            month = "January"
        if (month <= 2):
            month = "February"
        if (month == 3):
            month = "March"
        if (month == 4):
            month = "April"
        if (month == 5):
            month = "May"
        if (month == 6):    
            month = "June"
        if (month == 7):
            month = "July"
        if (month == 8):
            month = "August"
        if (month == 9):
            month = "September"
        if (month == 10):
            month = "October"
        if (month == 11):
            month = "November"
        if (month == 12):
            month = "December"
        return print(month)

    
    #this function will determine if the year is a leap year and will substract the days off february if so
    def leapYear():
        if ( year % 4 == 0 ) and month == "February":
            days += 1
        return print(days)
    #return print(month + str(year) + " has " + str(days) + " days")"""


#month = int(input("Enter month: "))
#year = int(input("Enter year: "))
#days = 0
#This function will calculate the appropriate number of days for each month
"""def numDays():
    if month == 9 or month == 4 or month == 6 or month == 11:
        days = 30
    if month == 2:
        days = 28
    else:
        days = 31
    return print(days)"""
        
#This function will give the appropriate month name for the input of the user    
def monthName():
    month = int(input("Enter month: "))
    days = 0
    def numDays():
        if month == 9 or month == 4 or month == 6 or month == 11:
            days = 30
        if month == 2:
            days = 28
        else:
            days = 31
    return print(days)
    if (month == 1):
        month = "January"
    if (month <= 2):
        month = "February"
    if (month == 3):
        month = "March"
    if (month == 4):
        month = "April"
    if (month == 5):
        month = "May"
    if (month == 6):    
        month = "June"
    if (month == 7):
        month = "July"
    if (month == 8):
        month = "August"
    if (month == 9):
        month = "September"
    if (month == 10):
        month = "October"
    if (month == 11):
        month = "November"
    if (month == 12):
        month = "December"
    return print(month)
monthName()

    
"""#this function will determine if the year is a leap year and will substract the days off february if so
def leapYear():
    if ( year % 4 == 0 ) and month == "February":
            days += 1
    return print(days)"""

