# Python program to check if
# given mobile number is valid
import re


def isValid(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("[6-9][0-9]")
    return Pattern.match(s)


# Driver Code
s = input("Enter the Phone number")
if (isValid(s)and len(s)==10):
    print("Valid Number")
else:
    print("Invalid Number")