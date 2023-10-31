"""
Flow control 
in  Python we can have one if and one else but unlimited elif s.
"""

x = 3

if x == 1:
    print("x is 1")
else:
    print("x is not equal to 1")

print("outside the if statement")

timeis = 21

if timeis < 12:
    print("Good Morning")
elif timeis < 20:
    print("Good afternoon!")
else:
    print("Good Night")