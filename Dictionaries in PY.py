"""Dictionaries in Python"""

user_dic = {
    'username' : "JQ",
    'name': 'John',
    'age': 42
}

print(user_dic)

print(user_dic.get("name"))

user_dic["married"] = True

print(user_dic)

print(len(user_dic))

user_dic.pop("married")
print(user_dic)

#user_dic.clear()
print(user_dic)
# del user_dic

for x in user_dic:
    print(x)

for x, y in user_dic.items():
    print(x, y)

user_dic2 = user_dic.copy() #making copy of dictionary and then editing
user_dic2.pop("age")
print(user_dic2)
