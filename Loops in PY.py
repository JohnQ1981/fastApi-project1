"""
for and while Loops

"""

my_list = [ 1,2,3,4,5,6,7,8,9,10]

for x in my_list:
    print(x)

for y in range( 45 , 90):
    print(y)

sum_of_range = 0
for x in my_list:
    sum_of_range += x
    print(sum_of_range)

print(f"Total is {sum_of_range}")

my_list_string = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for x in my_list_string:
    print(f"Happy {x}")

#While loops

i = 0
while i < 15:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 9:
        break
else:
    print("i is not larger or equal to 5")
