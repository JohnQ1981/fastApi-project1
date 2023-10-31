"""
Lists
"""

my_list = [80, 55 , 565, 1]
print(my_list)

people_list = ['Eric', 'Hello', 'Google']
print(people_list)

print(people_list[1])

print(my_list[3])

""" if we use -1 it prints the last item no matter how long the is the list"""
test_list = ['asdfd', 6, 'Hello', 54, 66, 33, 55,44, 66, 77, 'Eric']

print(test_list[-1])
""" Print the range"""
print(test_list[0:4])

""" inserting and deletion"""
people_list.append("John")
print(people_list)
my_list.insert(5, 1050)
print(my_list)
my_list.remove(1050)
print(my_list)
my_list.pop(0)
print(my_list)
print(len(my_list))