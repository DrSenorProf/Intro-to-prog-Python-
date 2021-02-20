# File: Payroll.py
# Student: Emiliano Villarreal
# UT EID: ev8559
# Course Name: CS303E
# 
# Date Created: 2/12/2021
# Date Last Modified: 2/12/2021
# Description of Program: This program will take input from the user to create a
# accurate payroll statement.

employeeName = input("Enter employee's name: ")
numHours = input("Enter number of hours worked in a week: ")
hourlyPayRate = input("Enter hourly pay rate: ")
federalTax = input("Enter federal tax withholding rate: ")
stateTax = input("Enter state tax withholding rate: ")
grossPay = float(numHours) * float(hourlyPayRate)
finalNumHours = format(float(numHours), "0.1f")
finalHourlyPayRate = format (float(hourlyPayRate),"0.2f")
finalGrossPay = format(grossPay, "0.2f")
fedPercentage = float(federalTax) 
fedPercent = format(fedPercentage, "0.1%")
fedWhithholdings = float(federalTax) * grossPay
finalFedWithholdings = format(fedWhithholdings, "0.2f")
statePercent = float(stateTax) 
finalStTaxPercent = format(statePercent, "0.1%")
stWithholdings = float(stateTax) * grossPay 
finalStWithholdings = format(stWithholdings,"0.2f")
totalDeductions =  stWithholdings + fedWhithholdings
finalDeductions = format( totalDeductions, "0.2f")
netPay = grossPay - float(finalDeductions) 
finalNetPay = format(netPay, "0.2f")


print("")
print("Employee name: " + employeeName)
print("Hours worked: " + finalNumHours)
print("Pay rate: $" + finalHourlyPayRate)
print("Gross pay: $" + finalGrossPay)
print("Deductions:  ")
print("  Federal withholding ("+ fedPercent +"): $" + finalFedWithholdings)
print("  State withholding (" + finalStTaxPercent + "): $" + finalStWithholdings)
print("  Total deductions: $" + finalDeductions)
print("Net pay: $" + finalNetPay)

