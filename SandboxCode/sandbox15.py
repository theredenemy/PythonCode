import os
endofcode = "###############################################################"
# Sandbox Starts here
anything = float(input("Enter a number:"))
something = anything ** 2.0
print(anything,"to the power of 2 is",something)
print(endofcode)
leg_a = float(input("Input first leg length:"))
leg_b = float(input("Input second leg length:"))
hypo = (leg_a**2 + leg_b**2)** .5
print("Hypotenuse length is", hypo)
print(endofcode)
firstNam = input("May i have your first name, please? ")
lastNam = input("May i have your last name, please? ")
print("Thank you.")
print("\nYour name is " + firstNam + " " + lastNam + ".")