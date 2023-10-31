"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""
my_dic ={

}
def my_f(firstname, lastname, age):
    my_dic["firsname"] = firstname
    my_dic["lastname"] = lastname
    my_dic["age"] = age
    print(my_dic)

my_f("Jo", "Qo", 40)

def user_dic(first, last, age):
    created_user_dic = {
        "firstname" : first,
        "lastname": last,
        "age": age
    }
    return created_user_dic

solution_dic = user_dic(first="John", last="Kuch", age= 45)

print(solution_dic)