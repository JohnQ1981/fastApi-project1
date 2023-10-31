"""
sets are similar to lists but are unordered and cannot contain duplications
"""
my_set = { 1,2,3,4,5,6,7,9,10, 1,2,3}
print(my_set)
print (len(my_set))
for x in my_set:
    print(x)

"""remove element from set"""
my_set.discard(3)
print (len(my_set))
my_set.clear()
print(my_set)
my_set.add("Hello")
print(my_set)
my_set.update([7,9999])
print(my_set)

""" Tuples are ordered but unchangeable """
my_tuple = ( 1,2,3,4,5,6,7)
print(my_tuple)