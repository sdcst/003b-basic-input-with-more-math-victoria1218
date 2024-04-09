#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

import math

a = float(input("Enter the first price:"))
b = float(input("Enter the second price:"))
c = float(input("Enter the third price:"))
d = float(input("Enter the fourth price:"))
e = float(input("Enter the fifth price:"))

t = a+b+c+d+e
tax = t*0.12
tx = round(tax,2)
tt = tx+t
print(f"Your subtotal is ${t} and your taxes total ${tax} for a total of ${tt}")

