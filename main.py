# Simple directory scanner
import os

# Getting input for path
path = input("What directory would you like scanned? ")
print("You got it, here we go. ")
# Initiating scan
scanned = os.listdir(path)
# Printing scanned directory
print(scanned)
