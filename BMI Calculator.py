'''
This is BMI Calculator
'''
print ('Welcome to BMI Calculator')
first_name = input('What is your first name ')
last_name = input('What is yourLast name ')
print(f" Hi {first_name} {last_name}, lets calculate your BMI (Body Mass Index)")
w = float(input('Enter your Weight in KGs '))
h = float(input("Enter your Height in CMs "))
bmi = float(10000*w)/(h*h)

print(f'Your BMI is {bmi}')
