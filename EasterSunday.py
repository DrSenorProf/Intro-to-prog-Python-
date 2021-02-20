# File: EasterSunday.py
# Student: Emiliano Villarreak
# UT EID: ev8559
# Course Name: CS303E
# 
# Date Created: 2/2/2021
# Date Last Modified: 2/2/2021
# Description of Program: This program will accuratley predict the exact month
# and day of Easter Sunday for year x

# This variable sets the year
y = int(input("Enter year: ")) 

a = y % 19

b = y // 100

c = y % 100

d = b // 4

e = b % 4

g = (8 * b + 13) // 25

h =  (19 * a + b - d - g + 15) % 30

j = c // 4

k = c % 4

m = (a + 11 * h) //319

r = (2 * e + 2 * j - k - h + m + 32) % 7

n =  (h - m + r + 90) // 25

p = (h - m + r + n + 19) % 32

print("In " + str (y) + " Easter Sunday is on month " + str(n)+ " and day " + str(p))
