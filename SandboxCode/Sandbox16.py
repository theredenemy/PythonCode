print("Setting Up Sandbox!")
endofcodevar = "###############################################################"
import os
def SandboxDir():
    os.system("dir")
    os.system("tree")

def endofcode():
    print(endofcodevar)

print("Done!")
# Sandbox Starts here
print("+" + 10 * "-" + "+")
print(("|" + "" * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
endofcode()
x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
