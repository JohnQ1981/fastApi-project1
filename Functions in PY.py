"""
Functions

"""

print("Welcome to Functions in Python")
"""Defined a function"""
def my_function():
    print("inside my function")

#called that function
my_function()

def my_f(name):
    print(f"Hello {name} !")

my_f('John')

def multiply_number(a, b):
    return a*b

solution = multiply_number(15, 8)

print(solution)
print(multiply_number(5, 8))

def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

number_list = [1,2,3,4,5,6,7,8,9]
print_list(number_list)

def buy_item(cost_of_item):
    return cost_of_item + add_tax(cost_of_item)

def add_tax(cost_of_item):
    current_tax_rate = 0.0835
    return cost_of_item * current_tax_rate

final_cost = buy_item(100)

print(final_cost)